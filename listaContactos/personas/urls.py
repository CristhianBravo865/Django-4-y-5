from django.urls import path
from .views import PersonaListView, PersonaDetailView, PersonaCreateView, PersonaUpdateView, PersonaDeleteView, PersonaQueryView

app_name = 'personas'

urlpatterns = [
    path('', PersonaListView.as_view(), name='persona-list'),
    path('<int:pk>', PersonaDetailView.as_view(), name='persona-detail'),
    path('create/', PersonaCreateView.as_view(), name='persona-create'),
    path('<int:pk>/update/', PersonaUpdateView.as_view(), name='persona-update'),
    path('<int:pk>/delete/', PersonaDeleteView.as_view(), name='persona-delete'),
    path('json/', PersonaQueryView.as_view(), name='persona-json'),
]
