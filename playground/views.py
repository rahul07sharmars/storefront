from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request -> response

def say_hello(request):
    return HttpResponse("Hello World")

def say_helloHtml(request):
    # return render(request, 'hello.html')
    return render(request, "hello.html", {"name": "rahul" })