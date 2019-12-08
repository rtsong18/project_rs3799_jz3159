from django.shortcuts import render, redirect
from django.http import HttpResponse 

# Create your views here.

def index(request):
    squirrels = squirrels.objects.all()
    context = {'squirrel_index':squirrels}
    return render(request, 'sightings/index.html',context)

def details(request,unique_squirrel_id):
    squirrel = squirrels.objects.get(unique_squirrel_id=snique_squirrel_id)
    context = {'squirrel':squirrel}
    return render(request, 'sightings/details.html',context)

def add(request):
    squirrel = squirrels.objects.all()
    context = {'squirrel_index':squirrel}
    return render(request, 'sightings/add.html',context)

def stats(request):
    squirrels = squirrels.objects.all()
    num_squirrels = squirrels.count()
    num_adult = squirrels.filter(age = 'Adult').count()
    num_color_gray = squirrels.filter(primary_fur_color = 'Gray').count()
    num_eating = squirrels.filter( eating = True ).count()
    num_lazy_squirrels = squirrels.filter(shift = 'PM').count()
    context = {
            'num_sqirrels':num_squirrels,
            'num_adult':num_adult,
            'num_color_gray':num_color_gray,
            'num_eating': num_eating,
            'num_lazy_squirrels' : num_lazy_squirrels,
            }
    return render(request, 'sightings/stats.html',context)

def update(request):
    squirrel = squirrels.objects.all()
    context = {'squirrel_index':squirrel}
    return render(request, 'sightings/update.html',context)
