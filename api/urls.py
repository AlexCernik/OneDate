from django.urls import path, include
from .api import Character_APIView,Character_APIView_Detail

app_name = 'Api'

urlpatterns = [
  path('api-rest/',Character_APIView.as_view(),name='api'),
  path('character/<int:pk>/',Character_APIView_Detail.as_view(),name='character'),
  # path('api/',characterList),
  # path('characters/<int:pk>/',characterDetail),
]

# urlpatterns = [
#   path('api/',CharacterAPI.as_view(),name='character'),
#   path('api-auth/', include('rest_framework.urls'))
# ]