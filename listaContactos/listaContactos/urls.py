from django.contrib import admin
from django.urls import path, include
from personas.views import myHomeView, anotherView

urlpatterns = [
    path('', myHomeView, name='PaginaInicio'),
    path('another/', anotherView, name='otra'),
    path('admin/', admin.site.urls),
    path('personas/', include('personas.urls', namespace='personas')),  # ✅ esta línea es clave
]
