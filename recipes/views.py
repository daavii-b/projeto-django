from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('Home Page')


def about(request):
    return HttpResponse('About')


def contact(request):
    return HttpResponse('Contact')
