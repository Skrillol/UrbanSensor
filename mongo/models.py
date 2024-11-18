from django.db import models

class Encuesta(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class Pregunta(models.Model):
    TIPO_RESPUESTA = [
        ('ALTERNATIVA', 'Alternativa'),
        ('TEXTO', 'Texto'),
    ]

    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)
    tipo_respuesta = models.CharField(max_length=20, choices=TIPO_RESPUESTA)

    def __str__(self):
        return self.texto

class Alternativa(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name="alternativas")
    texto = models.CharField(max_length=255)

    def __str__(self):
        return self.texto

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, blank=True, null=True)
    respuesta_texto = models.TextField(blank=True, null=True)
    respuesta_alternativa = models.ForeignKey(Alternativa, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Respuesta a: {self.pregunta.texto}"