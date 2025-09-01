from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

def home(request):
    return HttpResponse("Hello World")

def get_api_data(request, id) :
    api=