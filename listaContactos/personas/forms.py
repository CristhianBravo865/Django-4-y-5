from django import forms



from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'edad', 'donador']

class RawPersonaForm(forms.Form):
    nombres = forms.CharField(label='Tu nombre')
    apellidos = forms.CharField()
    edad = forms.IntegerField(initial=20)
    donador = forms.BooleanField(required=False)