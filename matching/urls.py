from django.urls import path
from .views import *

app_name="matching"

urlpatterns = [
    path('', matching_view,name="match"),
  

] 
