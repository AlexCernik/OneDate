from django.shortcuts import render
from django.http import Http404
from api.models import Character

# Create your views here.

def index(request):
  return render(request, 'section.html')