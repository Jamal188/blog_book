from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .utils import generate_secret_code, send_secret_code_email
from blogs.models import Blog, Comment, Like
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.core.exceptions import ValidationError
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

def left_column_view(request):
    context = {
            'user': request.user,
            }
    return render(request, 'users/left_column.html', context)

def mid_column_view(request):
    user_posts = Blog.objects.filter(author=request.user).order_by('-date_created')
    context = {
            'posts': user_posts,
            }
    return render(request, 'users/mid_column.html', context)

def right_column_view(request):
    return render(request, 'users/right_column.html')



def profile_view(request):    
     return render(request, 'users/profile.html')


@require_http_methods(["GET", "POST"])
def edit_field(request, field_name):
    user = request.user
    if request.method == "POST":
        try:
            value = request.POST.get(field_name)
            if field_name == 'date_of_birth':
                # Convert string to date object
                from datetime import datetime
                value = datetime.strptime(value, '%Y-%m-%d').date()
            
            setattr(user, field_name, value)
            user.full_clean()  # Validate all fields
            user.save()
            return render(request, 'users/field_display.html', {
                'user': user,
                'field_name': field_name
            })
        except (ValidationError, ValueError) as e:
            # Handle validation errors
            return render(request, 'users/field_edit.html', {
                'user': user,
                'field_name': field_name,
                'error': str(e)
            })
    
    # Handle cancel action
    if request.GET.get('cancel'):
        return render(request, 'users/field_display.html', {
            'user': user,
            'field_name': field_name
        })

    context = {
        'user': user,
        'field_name': field_name
    }
    
    response = render(request, 'users/field_edit.html', context)
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response



@require_http_methods(["GET", "POST"])
# views.py
def change_avatar(request):
    if request.method == "POST":
        # Handle upload logic
        return render(request, 'users/avatar_display.html', {'user': request.user})
    
    if request.GET.get('cancel'):
        # Return FULL display template (not partial form)
        return render(request, 'users/avatar_display.html', {'user': request.user})
    
    return render(request, 'users/avatar_edit.html')
