from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Anaê Ross',
    })


def about(request):
    return HttpResponse("This is my about page!")


def contact(request):
    return HttpResponse("This is my contact page, send us an email")



