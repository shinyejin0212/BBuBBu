from django.urls import path
from .views import *

app_name="adopt"

urlpatterns = [
    path('',adopt_main,name="adopt_main"),
    path('adopt_try/<int:id>', adopt_try,name="adopt_try"),
    path('adopting/<int:id>',adopting,name="adopting"),
] 
