from django.contrib import admin
from django.urls import path
from personas.views import personasTestView, personaCreateView, personasAnotherCreateView, anotherView, myHomeView

urlpatterns = [
    path('', myHomeView, name='PaginaInicio'),
    path('people/', personasTestView, name='personas'),
    path('add/', personaCreateView, name='AgregarPersonas'),
    path('anotherAdd/', personasAnotherCreateView, name='OtroAgregarPersonas'),
    path('another/', anotherView, name='otra'),
    path('admin/', admin.site.urls),
]
