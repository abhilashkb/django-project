from django.shortcuts import render
from django.http import HttpResponse
from .models import departments
# Create your views here.

def index(request):
    return render( request, 'index.html')
def booking(request):
    return render( request, 'booking.html')
def about(request):
    return render( request, 'about.html')
def doctors(request):
    return render( request, 'doctors.html')
def contact(request):
    return render( request, 'contact.html')
def department(request):
    dict_depart = { 
                   'dept': departments.objects.all()
                   }
    return render( request, 'department.html', dict_depart)
