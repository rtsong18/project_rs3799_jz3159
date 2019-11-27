from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('sightings/', include('sightings.urls')),
    path('admin/', admin.site.urls),
]
