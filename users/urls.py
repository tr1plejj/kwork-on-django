from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('profile/<slug:username>', views.profile, name='profile'),
    # path('login/', views.Login.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('edit_profile/', views.ProfileEdit.as_view(), name='edit_profile'),
    path('find_workers/', views.find_workers, name='find_workers'),
]
