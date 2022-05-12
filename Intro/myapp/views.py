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

def imagepage(request):
    return render(request, 'imagepage.html')

def imagepage2(request):
    return render(request, 'imagepage2.html')

def imagepage3(request):
    return render(request, 'imagepage3.html')

def imagepage4(request):
    return render(request, 'imagepage4.html')

def imagepage5(request, imagename):
    myimagename = str(imagename);
    myimagename = myimagename.lower();
    print(myimagename)
    if myimagename == "django":
        var = True
    elif myimagename =="python":
        var = False
    mydictionary = {
        "var" : var
    }
    return render(request, 'imagepage5.html', context=mydictionary)