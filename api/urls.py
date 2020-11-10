from django.urls import path, include, re_path
# from .api import Character_APIView,Character_APIView_Detail
from .api import get_characters_details, get_characters_lists, get_characters_alive, get_characters_dead

app_name = 'Api'

urlpatterns = [
  path('',get_characters_lists,name='api'),
  path('character/<int:pk>/',get_characters_details,name='character'),
  path('character/alive/',get_characters_alive,name='characters-alive'),
  path('character/dead/',get_characters_dead,name='characters-dead'),
]