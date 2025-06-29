from django.shortcuts import render, redirect
from .forms import RawPersonaForm, PersonaForm
from .models import Persona

def personasAnotherCreateView(request):
    form = PersonaForm()

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
        else:
            print(form.errors)

    return render(request, "another_add.html", {"form": form})

def personaCreateView(request):
    obj = Persona.objects.get(id=2)
    form = PersonaForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()

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
