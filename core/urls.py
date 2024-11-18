from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='test/', permanent=False)),  # Redirección desde '' a 'login'
    path('test/', views.test),  # Ruta hacia la vista de login
    path('test2/', views.test2),  # Ruta hacia la vista de login

    path('login/', views.login),
    path('login/menu/', views.menu),

    #Gestion de Encuestas
    path('encuestaNew', views.create_encuesta),
    path('encuestaEdite/<int:id>', views.edit_encuestaHTML),
    path('encuestaEdit', views.edit_encuesta),
    path('encuestaDelete/<int:id>', views.delete_encuesta),

    #Getion de Pregunta
    path('preguntaNew/<int:id>', views.create_preguntaHTML),
    path('preguntaCreate', views.create_pregunta),
    path('preguntaEdit/<int:id>', views.edit_preguntaHTML),
    path('preguntaEdit2', views.edit_pregunta),
    path('preguntaDelete/<int:id>', views.delete_pregunta),

    #Gestion de Alternativas
    path('alternativaNew/<int:id>', views.create_alternativaHTML),
    path('alternativaCreate', views.create_alternativa),
    path('alternativaEdit/<int:id>', views.edit_alternativaHTML),
    path('alternativaEdit2', views.edit_alternativa),
    path('alternativaDelete/<int:id>', views.delete_alternativa),

    #Gestion de Respuestas
    path('respuestaNew/<int:id>', views.create_respuestaHTML),
    path('respuestaCreate', views.create_respuesta),
    path('respuestaEdit/<int:id>', views.edit_respuestaHTML),
    path('respuestaEdit2', views.edit_respuesta),
    path('respuestaDelete/<int:id>', views.delete_respuesta),

    #Responder Encuesta
    path('encuestaResponder/<int:id>', views.responder_encuestaHTML),
    path('encuestaResponder2', views.guardar_encuesta),
 

]

'''
path('', RedirectView.as_view(url='login/', permanent=False)),  # Redirección desde '' a 'login'
path('login/', views.login),  # Ruta hacia la vista de login
path('login/menu/', views.menu)


path('encuestaList', views.list_encuesta, name='encuestaList'),
path('encuestaEdit/<int:id>', views.edit_encuesta, name='encuestaEdit'),
path('encuestaDelete/<int:id>', views.delete_encuesta, name='encuestaDelete'),
'''
