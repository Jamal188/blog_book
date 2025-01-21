from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('verify/<int:user_id>/', views.verify_code, name='verify_code'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

]


