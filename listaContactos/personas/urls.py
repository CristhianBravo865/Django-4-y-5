from django.urls import path
from .views import (
    personaCreateView,
    personasAnotherCreateView,
    personasListView,
    personasShowObject,
    personasDeleteView,
)

app_name = 'personas'

urlpatterns = [
    path('add/', personaCreateView, name='adding'),
    path('anotherAdd/', personasAnotherCreateView, name='another_add'),
    path('<int:myID>/', personasShowObject, name='browsing'),
    path('<int:myID>/delete/', personasDeleteView, name='deleting'),
    path('', personasListView, name='listing'),
]
