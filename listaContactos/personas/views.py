from django.shortcuts import get_object_or_404, render, redirect
from .forms import RawPersonaForm, PersonaForm
from .models import Persona
def personasShowObject(request, myID):
    obj = get_object_or_404(Persona, id=myID)
    context = {
        'objeto': obj,
    }
    return render(request, 'descripcion.html', context)

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
    initialValues = {
        'nombres': 'Sin Nombre'
    }
    form = PersonaForm(request.POST or None, initial=initialValues)

    if form.is_valid():
        form.save()
        form = PersonaForm(initial=initialValues)

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
