
from django.urls import path

from . import views


app_name = 'converter'
urlpatterns = [
  # Home page
  path('', views.index, name='index'),

  # Page that shows inputs
  path('input/', views.input, name='input'),

  # Detail page for result.
  path('result/', views.result, name='result'),
]

