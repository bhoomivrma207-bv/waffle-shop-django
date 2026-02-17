from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello world! You are at waffle and bhoomi Home Page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("hello world! You are at waffle and bhoomi About Page")

def contact(request):
    return HttpResponse("hello world! You are at waffle and bhoomi Contact Page")