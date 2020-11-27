from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse

from main_app.models import Vacancy
import json
import requests

def generate_description(request):
    data = json.loads(request.body)
    response = requests.post('http://localhost:7000/generate', data=data)
    return JsonResponse(response.json())