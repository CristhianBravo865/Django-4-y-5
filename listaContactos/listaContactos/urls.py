from django.contrib import admin
from django.urls import path
from personas.views import personaCreateView, personasAnotherCreateView, anotherView, myHomeView

urlpatterns = [
    path('', myHomeView, name='PaginaInicio'),
    path('add/', personaCreateView, name='AgregarPersonas'),
    path('anotherAdd/', personasAnotherCreateView, name='another_add'),
    path('another/', anotherView, name='otra'),
    path('admin/', admin.site.urls),
]
