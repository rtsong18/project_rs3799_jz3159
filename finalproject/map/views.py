from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import map

def index(request):
    squirrels = map.objects.all()
    context = {
            squirrels: 'squirrels'
            }
    return render(request,'map/index.html',context) 
