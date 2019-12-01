from django.shortcuts import render, redirect
from django.http import HttpResponse !!!!!!!!!!!!!!
from django.views.generic.edit import !!!!!!!!!!!!!!!!!!!! 

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






def details(request,unique_squirrel_id):
    squirrel = squirrels.objects.get(unique_squirrel_id=snique_squirrel_id)
    context = {'squirrel':squirrel}
    return render(request, 'sightings/details.html',context)



def stats(request):
    num_squirrels = squirrels.objects.all().count()
    
    context = {'num_sqirrels':num_squirrels}
    return render(request, 'sightings/stats.html',context)





def update(request):
    squirrel = squirrel.objects.all()
    context = {'squirrel_index':squirrel}
    return render(request, 'sightings/update.html',context)
