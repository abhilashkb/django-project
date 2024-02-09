from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render( request, 'index.html')
def booking(request):
    return HttpResponse("Booking page")
def about(request):
    return HttpResponse("About page")
def doctors(request):
    return HttpResponse("Doctors")
def contact(request):
    return HttpResponse("contact page")