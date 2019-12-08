from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import squirrels

def index(request):
    sightings= squirrels.objects.all()[0:10]
    return render(request,'map/index.html',{'sightings':sightings}) 

