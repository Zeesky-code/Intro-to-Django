from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def second(request):
    return render(request, 'second.html')

def third(request):
    var = "hello world"
    greeting = "hey, how are you"
    fruits = ["apple", "orange", "mango"]
    my_dictionary = {
        "var": var,
        "msg": greeting,
        "myfruits": fruits,
    }
    return render(request, 'third.html', context=my_dictionary)

def add(request, a, b):
    return HttpResponse(a+b)

def intro(request, name, age):
    mydictionary = {
        "name" :name,
        "age" : age
    }
    return JsonResponse(mydictionary)