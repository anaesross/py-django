from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the recipes index.")


def about(request):
    return HttpResponse("This is my about page!")


def contact(request):
    return HttpResponse("This is my contact page, send us an email")


