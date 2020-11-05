from rest_framework import serializers
from . import models

class CharacterSerializer(serializers.ModelSerializer):
  # photo_url = serializers.SerializerMethodField()
  class Meta:
    model = models.Character
    fields = '__all__'
  # def get_photo_url(self,image):
  #   request = self.context.get('request')
  #   photo_url = image.photo.url
  #   return request.build_absolute_url(photo_url)