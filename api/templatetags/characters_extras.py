from django import template
from api.models import Character
from django.http import Http404
from random import randint
# from django.db.models import Max
# import random

register = template.Library()

@register.simple_tag
def get_character_all():
  try:
    return Character.objects.all()
  except Character.DoesNotExist:
    return Http404


@register.simple_tag
def get_character_random():
  try:
    return Character.objects.filter(pk__range=(1,6)).order_by('?')
  except Character.DoesNotExist:
    return Http404

@register.simple_tag
def get_character_alive():
  try:
    return Character.objects.filter(status__contains='Alive')
  except Character.DoesNotExist:
    return Http404

@register.simple_tag
def get_character_dead():
  try:
    return Character.objects.filter(status__contains='Dead')
  except Character.DoesNotExist:
    return Http404