from django.urls import path
from .views import *

app_name='dormline'
urlpatterns = [
    path('main/',dorm_main,name="dorm_main"),
    path('view_random/<str:username>', view_random, name='view_random'),
    path('follow/<str:username>',follow, name='follow'),
] 
