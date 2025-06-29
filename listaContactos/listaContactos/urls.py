from django.contrib import admin
from django.urls import path, include
from personas.views import myHomeView, anotherView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personas/', include('personas.urls')),
]
