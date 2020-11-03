from django.urls import path, re_path
# from .api import CharacterList, CharacterDetail
from .views import *

app_name = 'core'

urlpatterns = [
  path('api/', Character_APIView.as_view()),
  path('api/character/<int:pk>', Character_APIView_Detail.as_view()),
]

# urlpatterns = [
#   re_path(r'^characters/$', CharacterList.as_view()),
#   re_path(r'^characters/(?P<pk>[0-9]+)/$', CharacterDetail.as_view()),
# ]