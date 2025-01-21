from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm
from django.utils import timezone


# create blog view
@login_required
def create_blog_view(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/users/profile') # return the blog list page
    else :
        form = BlogForm()
    return render(request, 'blogs/create_blog.html', {'form':form})

@login_required
def edit_blog_view(request, blog_id):
    post = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('blogs:detail_blog_view', blog_id=post.id)
    else :
        form = BlogForm(instance=post)

    return render(request,'blogs/edit_blog.html', {'form':form, 'post': post})

def blog_list(request):
    pass

@login_required
def delete_blog_view(request, blog_id):
    post = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        post.delete()
        return redirect('/users/profile')
    

@login_required
def detail_blog_view(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blogs/detail_view.html', {'blog': blog})


def welcome_view(request):
    return render(request, 'blogs/welcome.html')
