from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .utils import generate_secret_code, send_secret_code_email
from blogs.models import Blog
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():            
            user = form.save()
            login(request, user)
            return redirect('/users/profile')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def verify_code(request, user_id):

    user = BlogUser.objects.get(id=user_id)
    if request.method == 'POST':
        entered_code = request.POST.get('code')
        if entered_code == user.secret_code:
            user.secret_code = None
            user.save()
            login(request, user)
            return redirect('/users/profile')
        # if invalid code:
        else :
            return render(request, 'users/verify_code.html', {'error': 'Invalid code', 'user_id' : user_id})
    
    return render(request, 'users/verify_code.html', {'user_id': user_id})

        





def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Get the authenticated user
            login(request, user)  # Log the user in
            return redirect('/users/profile')  # Redirect to the home page
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/users/login')

def profile_view(request):
     user_posts = Blog.objects.filter(author=request.user).order_by('-date_created')
     context = {
        'posts': user_posts,  # Pass the posts to the template
    }
     return render(request, 'users/profile.html', context)

