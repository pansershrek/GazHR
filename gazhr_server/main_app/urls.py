from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.urls import path, reverse
from django.shortcuts import render

from main_app.api.get_jobs_list import get_jobs_list

urlpatterns = [
    path("api/get_jobs_list", get_jobs_list, name="api/get_jobs_list"),
]