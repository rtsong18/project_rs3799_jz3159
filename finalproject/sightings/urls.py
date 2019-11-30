from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.GET,name = 'sightings-get'),
    path('add',views.POST,name = 'sightings-add'),
    path('stats/' views.GET,name = 'sightings-stats'),
    path('admin/', admin.site.urls),
]
