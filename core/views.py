from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CharacterSerializer
from .models import Character
from django.http import Http404
from django.shortcuts import render

def index(request):
  return render(request, 'index.html')

def api(request):
  return render(request,'api.html')
class Character_APIView(APIView):
  def get(self, request, fortmat=None, *args, **kwargs):
    character = Character.objects.all()
    serializer = CharacterSerializer(character,many=True)

    return Response(serializer.data)

  def character(self,request, format=None):
    serializer = CharacterSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Character_APIView_Detail(APIView):
  def get_object(self,pk):
    try:
      return Character.objects.get(pk=pk)
    except Character.DoesNotExist:
      raise Http404

  def get(self,request,pk,format=None):
    character = self.get_object(pk)
    serializer = CharacterSerializer(character)
    return Response(serializer.data)

  def put(self,request,pk,format=None):
    character = self.get_object(pk)
    serializer = CharacterSerializer(character,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self,request,pk,format=None):
    character = self.get_object(pk)
    character.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
# Create your views here.
