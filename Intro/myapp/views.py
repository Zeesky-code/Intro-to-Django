from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *

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

def myform(request):
    return render(request,'myform.html')

def submitmyform(request):

    formdictionary = {
        "var1" : request.POST['mytext'],
        "var2" : request.POST['mytextarea'],
        "method" : request.method
    }
    return JsonResponse(formdictionary)

def myform2(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            mydictionary={
                "form" :  FeedbackForm()
            }
            errorflag = False
            Errors = []
            if title != title.upper():
                errorflag  = True
                errormsg = "Title should be in Capital"
                return render(request, 'myform2.html', context=mydictionary)
            else:
                mydictionary["success"]  =True
                mydictionary["successmsg"] = "Form Submitted"
                return render(request, 'myform2.html', context=mydictionary)
        else:
            mydictionary = {
                "form": form
            }
            return render(request, 'myform2.html', context=mydictionary)
    else:
        form = FeedbackForm()
        mydictionary = {
            "form": form
        }
        return render(request, 'myform2.html', context=mydictionary)

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            var = str("Hello " + username)
            return HttpResponse(var)
        else:
            mydictionary = {
                "form": form
            }
            return render(request, 'login.html', context=mydictionary)
    else:
        form = LoginForm()
        mydictionary = {
            "form": form
        }
        return render(request, 'login.html', context=mydictionary)

def error_404_view(request, exception):
    return render(request, '404.html')

