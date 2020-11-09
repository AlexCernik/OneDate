from django import template
from api.models import Character
# from django.db.models import Max
# import random

register = template.Library()

@register.simple_tag
def get_character_random():
  character = Character.objects.order_by('?')
  return character