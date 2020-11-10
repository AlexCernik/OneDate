from rest_framework import status
from rest_framework.views import APIView
from .serializers import CharacterSerializer
from rest_framework.response import Response
from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view

from .models import Character

serializer_class = CharacterSerializer

def get_object(pk):
  try:
    return Character.objects.get(pk=pk)
  except Character.DoesNotExist:
    raise Http404

# por id
@api_view(['GET'])
def get_characters_details(request,pk,format='json'):
  character = get_object(pk)
  serializer = serializer_class(character)
  return JsonResponse(serializer.data)

@api_view(['GET'])
def get_characters_lists(request, format=None, *args, **kwargs):
  character = Character.objects.all()
  serializer = serializer_class(character,many=True)
  return Response(serializer.data)

# @api_view(['GET'])
# def apiOverView(request):
#   api_urls = {
#     'name':'Monkey D Luffy',
#     'age':19,
#     'rank':'Supernova',
#     'state':'Alive',
#   }
#   return Response(api_urls)

# @api_view(['GET'])
# def characterList(request):
#   character = Character.objects.all()
#   serializer = CharacterSerializer(character,many=True)
#   return Response(serializer.data)
#   # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def characterDetail(request,pk):
#   character = Character.objects.get(id=pk)
#   serializer = CharacterSerializer(character,many=False)
#   return Response(serializer.data)

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