from django import template
from api.models import Character
from django.http import Http404
# from django.db.models import Max
# import random

register = template.Library()

@register.simple_tag
def get_character_random():
  try:
    return Character.objects.order_by('?')
  except Character.DoesNotExist:
    return Http404

@register.simple_tag
def get_character_alive():
  try:
    return Character.objects.filter(state__contains='Alive')
  except Character.DoesNotExist:
    return Http404

@register.simple_tag
def get_character_dead():
  try:
    return Character.objects.filter(state__contains='Dead')
  except Character.DoesNotExist:
    return Http404