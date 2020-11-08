from django.urls import path, include, re_path
from .api import Character_APIView,Character_APIView_Detail

app_name = 'Api'

urlpatterns = [
  path('',Character_APIView.as_view(),name='api'),
  path('character/<int:pk>/',Character_APIView_Detail.as_view(),name='character'),
]