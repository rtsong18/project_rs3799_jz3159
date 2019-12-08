from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index,name = 'index'),
    path('add', views.add,name = 'add'),
    path('stats', views.stats,name = 'stats'),
    path('<str:unique_squirrel_id>', views.details ,name = 'details'),
    path('<str:unique_squirrel_id>/update', views.update ,name = 'update'),
    path('test',views.test,name = 'test')
]
