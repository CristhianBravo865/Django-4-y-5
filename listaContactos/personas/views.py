from django.shortcuts import render, redirect
from .forms import PersonaForm 

def personasAnotherCreateView(request):
    form = PersonaForm()

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 

    context = {
        'form': form
    }
    return render(request, "another_add.html", context)


from django.shortcuts import render
from .forms import PersonaForm 

def myHomeView(request):
    return render(request, "home.html", {})

def personaCreateView(request):
    form = PersonaForm()
    return render(request, "persona_form.html", {"form": form})

def anotherView(request):
    return render(request, "otra_mas.html")
