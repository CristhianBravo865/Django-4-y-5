from django.shortcuts import render

# Create your views here.
from .forms import PersonaForm, RawPersonaForm
from django.shortcuts import render

def personasAnotherCreateView(request):
    form = RawPersonaForm()
    context = {
        'form': form,
    }
    return render(request, 'personas/personasCreate.html', context)
