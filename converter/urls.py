
from django.urls import path

from . import views


app_name = 'converter'
urlpatterns = [
  # Home page
  path('', views.index, name='index'),

  # Page that shows inputs
  path('input/', views.convert_currency, name='input'),

  # Detail page for result.
  path('result/', views.get_result, name='result'),
]
