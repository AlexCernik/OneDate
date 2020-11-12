from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
  path('',views.index, name='home'),
  path('help-us/',views.hepl_up,name='help-us'),
  path('documentation/',views.documentation,name='documentation')
]