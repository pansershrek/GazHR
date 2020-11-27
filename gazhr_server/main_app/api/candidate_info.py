from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse

from main_app.models import Candidate

import json


def candidate_info(request):
    try:
        data = json.loads(request.body)
        candidate_id = data.get("candidate_id", None)
        candidate = Candidate.objects.filter(id__in=[candidate_id])
        return JsonResponse({"status": 200, "data": candidate[0]})
    except:
        return JsonResponse({"status": 404})