from . import models
from rest_framework import serializers

class CharacterSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Character
    fields = (
      'name','image',
      'date_old','age',
      'race','rank',
      'fruit_name','fruit_type',
      'origin','attack',
      'occupation','description',
      'state',
      'sex','reward',
    )
    # exclude = ['is_remove','created','modified']