from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from .forms import RawPersonaForm, PersonaForm
from .models import Persona
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.http import JsonResponse

class PersonaQueryView(View):
    def get(self, request, *args, **kwargs):
        queryset = Persona.objects.filter(edad__lte=40)
        return JsonResponse(list(queryset.values()), safe=False)

class PersonaDeleteView(DeleteView):
    model = Persona
    success_url = reverse_lazy('personas:persona-list')
    template_name = 'persona_confirm_delete.html'

class PersonaUpdateView(UpdateView):
    model = Persona
    fields = ['nombres', 'apellidos', 'edad', 'donador']
    template_name = 'persona_form.html'
class PersonaCreateView(CreateView):
    model = Persona
    fields = ['nombres', 'apellidos', 'edad', 'donador']
    template_name = 'persona_form.html'

class PersonaDetailView(DetailView):
    model = Persona
    template_name = 'persona_detail.html'

class PersonaListView(ListView):
    model = Persona
    queryset = Persona.objects.filter(edad__gte=18)
    template_name = 'personaslista.html'

def personasDeleteView(request, myID):
    obj = get_object_or_404(Persona, id=myID)

    if request.method == 'POST':
        print("lo borro")
        obj.delete()
        return redirect('listing')

    context = { 'objeto': obj }
    return render(request, 'personasBorrar.html', context)

def personasListView(request):
    queryset = Persona.objects.all()
    context = {
        'objectList': queryset,
    }
    return render(request, 'personasLista.html', context)

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
