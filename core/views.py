from django.shortcuts import render, redirect
from postgres.models import CustomUser, CuestomRols, UsersPassword
from mongo.models import Encuesta,  Pregunta, Alternativa, Respuesta    
# Create your views here.
def login(request):
    return render(request, "login.html")

def menu(request):
    return render(request, "sistema/menu.html")

def test(request):
    tabla_Encuesta = Encuesta.objects.all()
    tabla_Pregunta = Pregunta.objects.all()
    tabla_Alternativa = Alternativa.objects.all()
    tabla_Respuesta = Respuesta.objects.all()
    return render(request, "encuesta\encuesta.html", {'tabla_Encuesta': tabla_Encuesta, 'tabla_Pregunta': tabla_Pregunta, 'tabla_Alternativa': tabla_Alternativa, 'tabla_Respuesta': tabla_Respuesta})

def test2(request):
    tabla_Encuesta = Encuesta.objects.all()
    tabla_Pregunta = Pregunta.objects.all()
    tabla_Alternativa = Alternativa.objects.all()
    tabla_Respuesta = Respuesta.objects.all()
    return render(request, "encuesta\encuestaNew.html", {'tabla_Encuesta': tabla_Encuesta, 'tabla_Pregunta': tabla_Pregunta, 'tabla_Alternativa': tabla_Alternativa, 'tabla_Respuesta': tabla_Respuesta})

#Encuesta gestion------------------------------------------------
def create_encuesta(request):
    if request.method == 'POST':
        titulo = request.POST.get('encuesta_titulo')
        descripcion = request.POST.get('encuesta_descripcion')
        encuesta = Encuesta.objects.create(titulo=titulo, descripcion=descripcion)
        return redirect('/')
    return render(request, 'encuesta/encuestaNew.html')

def edit_encuestaHTML(request, id):
    encuesta = Encuesta.objects.get(id=id)
    return render(request, 'encuesta/encuestaEdite.html', {'encuesta': encuesta})

def edit_encuesta(request):
    encuesta = Encuesta.objects.get(id=request.POST.get('encuesta_id'))
    if request.method == 'POST':
        encuesta.titulo = request.POST.get('encuesta_titulo')
        encuesta.descripcion = request.POST.get('encuesta_descripcion')
        encuesta.save()
        return redirect('/')
    return render(request, 'encuesta/encuestaEdite.html', {'encuesta': encuesta})

def delete_encuesta(request, id):
    encuesta = Encuesta.objects.get(id=id)
    encuesta.delete()
    return redirect('/')

#Gestion de Preguntas-----------------------------------------------------
def create_preguntaHTML(request, id):
    encuesta = Encuesta.objects.get(id=id)
    return render(request, 'encuesta/preguntaNew.html', {'encuesta': encuesta})

def create_pregunta(request):
    if request.method == 'POST':
        id = request.POST.get('id_pregunta')
        texto = request.POST.get('pregunta_titulo')
        tipo_respuesta = request.POST.get('tipo_respuesta')

        encuesta = Encuesta.objects.get(id=id)

        respuesta = Pregunta.objects.create(encuesta=encuesta, texto=texto, tipo_respuesta=tipo_respuesta)
        return redirect('/')
    return render(request, 'encuesta/preguntaNew.html')

def edit_preguntaHTML(request, id):
    pregunta = Pregunta.objects.get(id=id)
    encuesta = pregunta.encuesta
    return render(request, 'encuesta/preguntaEdite.html', {'pregunta': pregunta, 'encuesta': encuesta})

def edit_pregunta(request):
    if request.method == 'POST':
        id = request.POST.get('id_pregunta')
        texto = request.POST.get('pregunta_titulo')
        tipo_respuesta = request.POST.get('tipo_respuesta')

        pregunta = Pregunta.objects.get(id=id)
        pregunta.texto = texto
        pregunta.tipo_respuesta = tipo_respuesta
        pregunta.save()
        return redirect('/')
    
    return render(request, 'encuesta/preguntaEdite.html')

def delete_pregunta(request, id):
    pregunta = Pregunta.objects.get(id=id)
    pregunta.delete()
    return redirect('/')

#Gestion de Alternativas--------------------------------------------------------
def create_alternativaHTML(request, id):
    pregunta = Pregunta.objects.get(id=id)
    encuesta = pregunta.encuesta
    return render(request, 'encuesta/alternativaNew.html', {'pregunta': pregunta, 'encuesta': encuesta})

def create_alternativa(request):
    if request.method == 'POST':
        id_pregunta = request.POST.get('id_pregunta')
        pregunta = Pregunta.objects.get(id=id_pregunta)


        texto = request.POST.getlist('alternativas[]')

        for texto in texto:
            if texto.strip():  # Evitar guardar alternativas vacías
                Alternativa.objects.create(pregunta=pregunta, texto=texto.strip())    

        return redirect('/')
    return render(request, 'encuesta/alternativaNew.html')

def edit_alternativaHTML(request, id):
    alternativa = Alternativa.objects.get(id=id)
    pregunta = alternativa.pregunta
    encuesta = pregunta.encuesta

    return render(request, 'encuesta/alternativaEdite.html', {'alternativa': alternativa, 'pregunta': pregunta, 'encuesta': encuesta})

def edit_alternativa(request):
    if request.method == 'POST':
        id = request.POST.get('id_alternativa')
        texto = request.POST.get('alternativa_texto')

        alternativa = Alternativa.objects.get(id=id)
        alternativa.texto = texto
        alternativa.save()
        return redirect('/')
    return render(request, 'encuesta/alternativaEdite.html')

def delete_alternativa(request, id):
    alternativa = Alternativa.objects.get(id=id)
    alternativa.delete()
    return redirect('/')


#Gestion de Respuestas--------------------------------------------------------
def create_respuestaHTML(request, id):
    pregunta = Pregunta.objects.get(id=id)
    encuesta = pregunta.encuesta
    return render(request, 'encuesta/respuestaNew.html', {'pregunta': pregunta, 'encuesta': encuesta})

def create_respuesta(request):
    if request.method == 'POST':
        id_pregunta = request.POST.get('id_pregunta')
        pregunta = Pregunta.objects.get(id=id_pregunta)

        if pregunta.tipo_respuesta == 'ALTERNATIVA':
            alternativa_id = request.POST.get('alternativa')
            alternativa = Alternativa.objects.get(id=alternativa_id)
            respuesta = Respuesta.objects.create(pregunta=pregunta, respuesta_alternativa=alternativa)
        elif pregunta.tipo_respuesta == 'TEXTO':
            respuesta_texto = request.POST.get('respuesta_texto')
            respuesta = Respuesta.objects.create(pregunta=pregunta, respuesta_texto=respuesta_texto)

        return redirect('/')
    return render(request, 'encuesta/respuestaNew.html')

def edit_respuestaHTML(request, id):
    respuesta = Respuesta.objects.get(id=id)
    pregunta = respuesta.pregunta
    encuesta = pregunta.encuesta

    return render(request, 'encuesta/respuestaEdite.html', {'respuesta': respuesta, 'pregunta': pregunta, 'encuesta': encuesta})

def edit_respuesta(request):
    if request.method == 'POST':
        id = request.POST.get('id_respuesta')
        respuesta_texto = request.POST.get('respuesta_texto')

        respuesta = Respuesta.objects.get(id=id)
        respuesta.respuesta_texto = respuesta_texto
        respuesta.save()
        return redirect('/')
    return render(request, 'encuesta/respuestaEdite.html')

def delete_respuesta(request, id):
    respuesta = Respuesta.objects.get(id=id)
    respuesta.delete()
    return redirect('/')

#Responder Encuesta
def responder_encuestaHTML(request, id):
    encuesta = Encuesta.objects.get(id=id)
    preguntas = Pregunta.objects.filter(encuesta=encuesta)
    alternativas = Alternativa.objects.all()
    return render(request, 'encuesta/respuestaEncuesta.html', {'encuesta': encuesta, 'preguntas': preguntas, 'alternativas': alternativas})

def guardar_encuesta(request):
    if request.method == 'POST':
        encuesta_id = request.POST.get('encuesta_id')
        encuesta = Encuesta.objects.filter(id=encuesta_id).first()

        if not encuesta:
            # Si no existe la encuesta, redirigir o manejar el error.
            return redirect('error_page')  # Cambia esto a la vista de error que prefieras.

        # Iterar sobre las preguntas relacionadas con la encuesta
        for pregunta in encuesta.pregunta_set.all():
            respuesta_key = f'respuesta_{pregunta.id}'

            # Si la pregunta es de tipo "ALTERNATIVA"
            if pregunta.tipo_respuesta == 'ALTERNATIVA':
                alternativa_id = request.POST.get(respuesta_key)
                if alternativa_id:  # Verificar si se seleccionó una alternativa
                    alternativa = Alternativa.objects.filter(id=alternativa_id).first()
                    if alternativa:
                        Respuesta.objects.create(
                            pregunta=pregunta,
                            respuesta_alternativa=alternativa
                        )
            
            # Si la pregunta es de tipo "TEXTO"
            elif pregunta.tipo_respuesta == 'TEXTO':
                respuesta_texto = request.POST.get(respuesta_key)
                if respuesta_texto:  # Verificar si se ingresó texto
                    Respuesta.objects.create(
                        pregunta=pregunta,
                        respuesta_texto=respuesta_texto
                    )

        # Redirigir tras guardar las respuestas
        return redirect('/')
    
    # Manejar solicitudes GET (opcional)
    return render(request, 'encuesta/respuestaEdite.html')
