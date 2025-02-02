from django import forms
from .models import Blog, Comment




class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ['title', 'content'] # fields included


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content_comment']
