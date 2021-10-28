from django.urls import path
from .views import *

app_name="matching"

urlpatterns = [
    path('', match_view,name="match_view"),
    path("match_upline/<int:id>",match_view, name="match_upline" ),
    # path("school_line/<int:id>",shcool_line, name="school_line" ),

] 
