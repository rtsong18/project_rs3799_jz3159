from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index,name = 'index'),
    path('add', views.add,name = 'add'),
    path('stats/', views.stats,name = 'stats'),
    path('sightings/<int:unique-squirrel-id>/', views.details,name = 'detail'),
    path('sightings/<int:unique-squirrel-id>/update', views.update ,name = 'update'),
]
