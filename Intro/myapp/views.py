from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World!")

def add(request, a, b):
    return HttpResponse(a+b)

def intro(request, name, age):
    mydictionary = {
        "name" :name,
        "age" : age
    }
    return JsonResponse(mydictionary)