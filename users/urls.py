from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('verify/<int:user_id>/', views.verify_code, name='verify_code'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('left-column/', views.left_column_view, name='left_column'),
    path('mid-column/', views.mid_column_view, name='mid_column'),
    path('right-column/', views.right_column_view, name='right_column'),
    path('profile/', views.profile_view, name='profile'),
    path('edit-field/<str:field_name>/', views.edit_field, name='edit_field'),
    path('change-avatar/', views.change_avatar, name='change_avatar'),

]


