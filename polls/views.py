from django.shortcuts import render

# Create your views here.

# write my first view

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world! \n this is Hesam akbari \n you are a the polls index")