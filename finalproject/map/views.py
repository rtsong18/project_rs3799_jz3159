from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import squirrels

def index(request):
    squirrelss = squirrels.objects.all()
    context = {
            squirrelss: 'squirrelss'
            }
    return render(request,'map/index.html',context) 
