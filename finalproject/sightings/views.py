from django.shortcuts import render, redirect
from django.http import HttpResponse !!!!!!!!!!!!!!
from django.views.generic.edit import !!!!!!!!!!!!!!!!!!!! 

# Create your views here.

def index(request):
    squirrels = squirrel.object.all()
    context = {'squirrel_index':squirrels}
    return render(request, 'sightings/index.html',context)






def add(request):
    squirrel = squirrel.object.all()
    context = {'squirrel_index':squirrel}
    return render(request, 'sightings/add.html',context)





def delete(request):
    squirrel = squirrel.object.all()
    context = {'squirrel_index':squirrel}
    return render(request, 'sightings/delete.html',context)






def details(request):
    squirrel = squirrel.object.all()
    context = {'squirrel_index':squirrel}
    return render(request, 'sightings/details.html',context)









def update(request):
    squirrel = squirrel.object.all()
    context = {'squirrel_index':squirrel}
    return render(request, 'sightings/update.html',context)
