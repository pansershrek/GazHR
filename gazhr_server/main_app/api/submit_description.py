from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.utils import timezone
from main_app.models import Vacancy
import json
import requests


def submit_description(request):
    data = json.loads(request.body)
    model_response = requests.post('http://localhost:7000/generate', data=data).json()

    vacancy = Vacancy(
        source_text=data['text'],
        transfored_text=model_response['description'],
        created_timestamp=timezone.now()
    )
    vacancy.save()

    return JsonResponse({
        'job_id': vacancy.id
    })