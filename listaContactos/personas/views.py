from django.shortcuts import render, redirect
from .forms import RawPersonaForm
from .models import Persona

def personasAnotherCreateView(request):
    if request.method == "GET":
        form = RawPersonaForm()
    
    elif request.method == "POST":
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            Persona.objects.create(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                edad=form.cleaned_data['edad']
            )
            return redirect('/')  
    
    context = {
        'form': form
    }
    return render(request, 'another_add.html', context)

def myHomeView(request):
    return render(request, "home.html", {})

def personaCreateView(request):
    form = PersonaForm()
    return render(request, "persona_form.html", {"form": form})

def anotherView(request):
    return render(request, "otra_mas.html")
