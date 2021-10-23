from django.urls import path
from .views import *

app_name="conversation"

urlpatterns = [
    path('',talk_page,name="talk_page"),
    path('create_talk/',create_talk,name="create_talk"),
    path('edit_talk/<int:talk_id>',edit_talk,name="edit_talk"),
    path('update_talk/<int:talk_id>',update_talk,name="update_talk"),
    path('delete_talk/<int:talk_id>',delete_talk,name="delete_talk"),

] 
