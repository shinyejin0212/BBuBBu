from django.urls import path
from .views import *

app_name='dormline'
urlpatterns = [
    path('view_random/<str:id>', view_random, name='view_random'),
    path('follow/<str:id>',follow, name='follow'),
] 
