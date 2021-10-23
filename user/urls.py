from django.urls import path
from .views import *

app_name="user"
urlpatterns = [
    path('login',login_view, name='login'),
    path('signup/',signup_view,name='signup'),
    path("main/", main, name='main'),
    path("logout/", logout_view, name='logout'),
    path('profile/<str:username>', profile, name='profile'),
    path('edit/<str:username>', edit, name='edit'),
    path('update_profile/<str:username>', update_profile, name='update_profile'),

] 
