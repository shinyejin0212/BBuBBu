from django.urls import path
from .views import *

app_name="adopt"

urlpatterns = [
    path('',main,name="main"),
    path('adopt_try/<int:id>', adopt_try,name="adopt_try"),

] 
