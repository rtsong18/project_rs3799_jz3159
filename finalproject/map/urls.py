from django.urls import path

from . import views

urlpatterns = [
        path('', views.GET, name='map'),
]
