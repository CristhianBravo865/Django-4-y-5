from django.urls import path
from .views import (
    personaCreateView,
    personasAnotherCreateView,
    personasListView,
    personasShowObject,
    personasDeleteView,
    PersonaListView,
)

app_name = 'personas'

urlpatterns = [
    path('', PersonaListView.as_view(), name='persona-list'), 
    path('<int:myID>/', personasShowObject, name='browsing'), 
]