from django.shortcuts import render, redirect
from django.http import HttpResponse 

# Create your views here.

def index(request):
    squirrels = squirrels.objects.all()
    context = {'squirrel_index':squirrels}
    return render(request, 'sightings/index.html',context)






def add(request):
    squirrel = squirrels.objects.all()
    context = {'squirrel_index':squirrel}
    return render(request, 'sightings/add.html',context)





def delete(request):
    squirrel = squirrels.objects.all()
    context = {'squirrel_index':squirrel}
    return render(request, 'sightings/delete.html',context)






def details(request):
    squirrel = squirrels.objects.all()
    context = {'squirrel_index':squirrel}
    return render(request, 'sightings/details.html',context)









def update(request):
    squirrel = squirrels.objects.all()
    context = {'squirrel_index':squirrel}
    return render(request, 'sightings/update.html',context)
