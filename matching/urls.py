from django.urls import path
from .views import *

app_name="matching"

urlpatterns = [
<<<<<<< HEAD
    path('', match_view,name="match_view"),
    path("match_upline/<int:id>",match_view, name="match_upline" ),
=======
    path("match_upline/<int:id>",match_view, name="match_view" ),
>>>>>>> d0ad08e104a459472ccb83f94a842f08bad92073
    # path("school_line/<int:id>",shcool_line, name="school_line" ),

] 