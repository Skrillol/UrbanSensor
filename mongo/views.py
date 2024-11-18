# encuestas_app/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Survey, Question
import json

@csrf_exempt
def create_survey(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get("title")
        description = data.get("description")
        question_data = data.get("questions", [])

        questions = [
            Question(
                question_text=q["question_text"],
                type=q["type"],
                options=q.get("options", [])
            ) for q in question_data
        ]

        survey = Survey(
            title=title,
            description=description,
            questions=questions
        )
        survey.save()
        return JsonResponse({"message": "Encuesta creada exitosamente"}, status=201)

    return JsonResponse({"error": "Método no permitido"}, status=405)
