from rest_framework import generics
from .serializers import CharacterSerializer
from django.http import JsonResponse, Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes

from .models import Character

serializer_class = CharacterSerializer

#simple repuesta en object Json
def get_destined_api(request):
  api_url = {
    "characters":"https://apionepiece.herokuapp.com/api/characters/"
  }
  return JsonResponse(api_url)

# obtener id desde la db
def get_object(pk):
  try:
    return Character.objects.get(pk=pk)
  except Character.DoesNotExist:
    raise Http404

# por id
@api_view(['GET'])
def get_characters_details(request,pk):
  character = get_object(pk)
  serializer = serializer_class(character)
  return JsonResponse(serializer.data)

# peticiones a todos los personajes
class Get_characters_all(generics.ListAPIView):
  queryset = Character.objects.all()
  serializer_class = CharacterSerializer
  renderer_classes = [JSONRenderer]

# buscando por los personajes que esten vivos
@api_view(['GET'])
def get_characters_alive(request,format=None):
  try:
    character = Character.objects.all().filter(status__contains='Alive')
    if character:
      serializer = serializer_class(character,many=True)
      return JsonResponse(serializer.data, safe=False)
    return JsonResponse({"Error":"DoesNotExist"})
  except Character.DoesNotExist:
    raise Http404

# buscando por los personajes que esten muertos
@api_view(['GET'])
def get_characters_dead(request,format=None):
  try:
    character = Character.objects.all().filter(status__contains='Dead')
    if character:
      serializer = serializer_class(character,many=True)
      return JsonResponse(serializer.data, safe=False)
    return JsonResponse({"Error":"DoesNotExist"})
  except Character.DoesNotExist:
    raise Http404
