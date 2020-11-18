from rest_framework import status
from rest_framework.views import APIView
from .serializers import CharacterSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.core import serializers
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse, Http404,HttpResponse
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

@api_view(['GET'])
def get_characters_alive(request,format=None):
  try:
    character = Character.objects.all().filter(status__contains='Alive')
    if character:
      serializer = serializer_class(character,many=True)
      return JsonResponse(serializer.data, safe=False)
    return JsonResponse({"Error":"DoesNotExist"})
  except Character.DoesNotExist:
    return Http404

@api_view(['GET'])
def get_characters_dead(request,format=None):
  try:
    character = Character.objects.all().filter(status__contains='Dead')
    if character:
      serializer = serializer_class(character,many=True)
      return JsonResponse(serializer.data, safe=False)
    return JsonResponse({"Error":"DoesNotExist"})
  except Character.DoesNotExist:
    return Http404

# class Character_APIView(APIView):
#   """ API VIEW DE PRUEBA """
#   serializer_class = CharacterSerializer

#   def get(self, request, fortmat=None, *args, **kwargs):
#     character = Character.objects.all()
#     serializer = self.serializer_class(character,many=True)

#     return Response(serializer.data)

#   def character(self,request, format=None):
#     serializer = self.serializer_class(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data,status=status.HTTP_201_CREATED)
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class Character_APIView_Detail(APIView):
#   """ API VIEW DE PRUEBA """
#   serializer_class = CharacterSerializer

#   def get_object(self,pk):
#     try:
#       return Character.objects.get(pk=pk)
#     except Character.DoesNotExist:
#       raise Http404

#   def get(self,request,pk,format=None):
#     character = self.get_object(pk)
#     serializer = self.serializer_class(character)
#     return Response(serializer.data)

#   def put(self,request,pk,format=None):
#     character = self.get_object(pk)
#     serializer = self.serializer_class(character,data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#   def delete(self,request,pk,format=None):
#     character = self.get_object(pk)
#     character.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)