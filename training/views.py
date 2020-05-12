from django.shortcuts import render, HttpResponse
import datetime

def index(request): 
    menu = ['esempi','blog']
    context = {
        'menu': menu,
    }
    return render(request, "index.html", context)