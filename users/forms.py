from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BlogUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)
    date_of_birth = forms.DateField(required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = BlogUser
        fields = ('username', 'email', 'password1', 'password2', 'phone_number', 'date_of_birth', 'profile_picture')
