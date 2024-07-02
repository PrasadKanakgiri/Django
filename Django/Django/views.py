from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello!!! You are at Django Home page")

def about(request):
    return HttpResponse("Hello!!! You are at Django About page")

def contact(request):
    return HttpResponse("Hello!!! You are at Django Contact page")
