from django.urls import path
from . import api

app_name = 'Api'

urlpatterns = [
  path('',api.get_destined_api,name='api'),
  path('characters/',api.Get_characters_all.as_view(),name="characters"),
  path('character/<int:pk>/',api.get_characters_details,name='character_pk'),
  path('character/alive/',api.get_characters_alive,name='characters-alive'),
  path('character/dead/',api.get_characters_dead,name='characters-dead'),
]