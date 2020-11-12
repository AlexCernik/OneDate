from django.shortcuts import render
from django.http import Http404
from api.models import Character

# Create your views here.

def index(request):
  return render(request, 'section.html')

def hepl_up(request):
  return render(request, 'html-extra/help_us.html')

def documentation(request):
  return render(request,'html-extra/documentation.html')