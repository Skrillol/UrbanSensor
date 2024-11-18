from django.contrib import admin
from .models import Encuesta, Pregunta, Respuesta, Alternativa

admin.site.register(Encuesta)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Alternativa)
