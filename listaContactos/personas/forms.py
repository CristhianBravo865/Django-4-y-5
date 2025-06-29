from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'edad', 'donador']

    def clean_nombres(self):
        nombre = self.cleaned_data.get('nombres')
        if nombre.istitle():
            return nombre
        raise forms.ValidationError('El nombre debe empezar con mayúscula.')

    def clean_apellidos(self):
        apellido = self.cleaned_data.get('apellidos')
        if apellido.istitle():
            return apellido
        raise forms.ValidationError('El apellido debe empezar con mayúscula.')

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad >= 18:
            return edad
        raise forms.ValidationError('Debe ser mayor de 18 años.')

class RawPersonaForm(forms.Form):
    nombres = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Sólo tu nombre, por favor',
            'id': 'nombreID',
            'class': 'special',
            'cols': '10',
        })
    )
    apellidos = forms.CharField()
    edad = forms.IntegerField(initial=20)
    donador = forms.BooleanField(required=False)
