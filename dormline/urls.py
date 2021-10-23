from django.urls import path
from .views import *

app_name="dormline"
urlpatterns = [
    path('dormmain/',dorm_main,name="dorm_main"),

] 
