from django.urls import path
from .views import *

app_name="stories"

urlpatterns = [
    path('detail',detail,name="detail"),
] 
