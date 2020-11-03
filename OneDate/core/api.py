from . import models, serializers

from rest_framework import generics

class CharacterList(generics.ListCreateAPIView):
  queryset = models.Character.objects.all()
  serializer_class = serializers.CharacterSerializer

class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = models.Character.objects.all()
  serializer_class = serializers.CharacterSerializer