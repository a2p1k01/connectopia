from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('register/', views.register_user, name='register'),
    path('users/', views.get_users, name='get_users'),
]
