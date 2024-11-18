# encuestas_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('crear_encuesta/', views.create_survey, name='create_survey'),
]
