from django.urls import path
from .views import *

app_name="stories"

urlpatterns = [
    path('storylist/',storylist,name="storylist"),
    path('detail',detail,name="detail"),
] 
