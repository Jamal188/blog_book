from django.urls import path
from . import views
app_name = 'blogs'

urlpatterns = [
        
        path('create/', views.create_blog_view, name='create_blog_view'),
        path('edit/<int:blog_id>/', views.edit_blog_view, name='edit_blog_view'),
        path('delete/<int:blog_id>/', views.delete_blog_view, name='delete_blog_view'),
        #path('detail/<int:blog_id>',views.detail_blog_view, name='detail_blog_view'),
        path('detail22/<int:blog_id>',views.detail_blog_view22, name='detail_blog_view22'),
        path('blog/<int:blog_id>/', views.detail_blog_view, name='detail_blog_view'),
        path('comment/<int:blog_id>/',views.handle_comment, name='handle_comment'),
        path('like/<int:blog_id>/', views.toggle_like, name='toggle_like'),
        path('load_comments/<int:blog_id>/', views.load_comments, name='load_comments'),
        path('load_likes/<int:blog_id>/', views.load_likes, name='load_likes'),
        ]
