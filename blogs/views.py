from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog, Comment, Like
from .forms import BlogForm, CommentForm
from django.utils import timezone
from django.http import JsonResponse
from django.core.serializers import serialize



@login_required
def create_blog_view(request):
    if request.method == 'POST':  # ensuring post method is used
        form = BlogForm(request.POST)
        if form.is_valid():       # ensuring the safety of the data
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/users/profile') # return the blog list page
    else :
        form = BlogForm() 
    return render(request, 'blogs/create_blog.html', {'form':form})

@login_required
def edit_blog_view(request, blog_id):
    post = get_object_or_404(Blog, id=blog_id)  # checking if the object exists 
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('/users/profile')
    else :
        form = BlogForm(instance=post)

    return render(request,'blogs/edit_blog.html', {'form':form, 'post': post})



@login_required
def delete_blog_view(request, blog_id):
    post = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        post.delete()
        return redirect('/users/profile')
@login_required
def detail_blog_view(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comment_form = CommentForm()
    context = {'blog': blog,'comment_form': comment_form,}
    return render(request, 'blogs/detail_view.html', context)

@login_required
def detail_blog_view22(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = blog.comment_set.all().order_by('-date_created')
    
    # Handle like POST
    if request.method == 'POST' and 'like' in request.POST:
        if request.user.is_authenticated:
            if request.user in blog.likes.all():
                blog.likes.remove(request.user)
            else:
                blog.likes.add(request.user)
        return redirect('blogs:detail_blog_view22', pk=blog.id)
    
    # Handle comment POST
    if request.method == 'POST' and 'comment' in request.POST:
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            Comment.objects.create(
                blog=blog,
                user=request.user,
                content_comment=form.cleaned_data['content_comment']
            )
            return redirect('blogs:detail_blog_view22', pk=blog.id)
    else:
        form = CommentForm()

    context = {
        'blog': blog,
        'comment_form': form,
        'comments': comments[:1]  # Show first comment initially
    }
    return render(request, 'blogs/detail_view22.html', context)



def welcome_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'blogs/welcome.html')

@login_required
def home(request):
    blogs = Blog.objects.all().order_by('-date_created')
    return render(request, 'blogs/home.html', {'blogs':blogs})




@login_required
def load_blogs(request):
    posts = Blog.objects.all().order_by('-date_created') # getting all the blogs posts from the db
    posts_data = []
    for post in posts:
        posts_data.append({
            "title": post.title,
            "content": post.content,
            "author": post.author.username,  # Include the author's username
            "date_created": post.date_created.isoformat(),  # Format the date
        })
    return JsonResponse(posts_data, safe=False)  # Return the custom JSON response
    




@login_required
def load_comments(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = blog.comments.all().order_by('-date_created_comment')
    comment_form = CommentForm()
    context = {'comments': comments , 'comment_form':comment_form, 'blog':blog}
    return render(request, 'blogs/comments.html', context)


@login_required
def handle_comment(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()
            return render(request, 'blogs/partials/comment.html', {'comment': comment})
        return JsonResponse({'error': 'Invalid comment'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def toggle_like(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    
    if request.method == 'POST':
        # Handle like toggling (create/delete)
        like, created = Like.objects.get_or_create(blog=blog, user=request.user)
        if not created:
            like.delete()
            liked = False
        else:
            liked = True
    else:
        # Handle GET: Check if the user has already liked the blog (no modification)
        liked = Like.objects.filter(blog=blog, user=request.user).exists()
    
    # Return the updated like status/count (safe for both GET and POST)
    context = {
        'blog': blog,
        'liked': liked,
        'csrf_token': request.META.get('CSRF_COOKIE', '')
    }
    return render(request, 'blogs/partials/like_count.html', context)




@login_required
def load_likes(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    likes = blog.likes.all()
    return render(request, 'blogs/likes.html', {'likes': likes})
