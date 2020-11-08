from django.urls import path
from . import views

app_name = 'Core'

urlpatterns = [
  path('',views.index, name='home'),
]