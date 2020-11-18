from rest_framework import serializers
from . import models

class CharacterSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Character
    fields = '__all__'