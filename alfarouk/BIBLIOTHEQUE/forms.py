from .models import *
from django.forms import ModelForm
from django import forms


class DomainesForm(ModelForm):
    class Meta:
        model = Domaines
        fields = ['domaines']
        widgets = {
  			'domaines':  forms.TextInput(attrs={'class': 'form-control', "id":"first-name-icon"}),
        }

class AuteursForm(ModelForm):
    class Meta:
        model = Auteurs
        fields = '__all__'
        widgets = {
  			'auteur':  forms.TextInput(attrs={'class': 'form-control', "id":"first-name-icon"}),
        }

class BlocsForm(ModelForm):
    class Meta:
        model = Blocs
        fields = ['bloc']
        widgets = {
  			'bloc':  forms.TextInput(attrs={'class': 'form-control', "id":"first-name-icon"}),
        }

class RayonsForm(ModelForm):
    class Meta:
        model = Rayons
        fields = ['rayon']
        widgets = {
  			'rayon':    forms.TextInput(attrs={'class': 'form-control', "id":"first-name-icon"}),
        }

class LivresForm(ModelForm):
    class Meta:
        model = Livres
        fields = ['titre','exemplaires']
        
        widgets = {
			  'titre':    forms.TextInput(attrs={'class': 'form-control', "id":"first-name-icon", "placeholder":"Titre du livre"}),
        'exemplaires': forms.NumberInput(attrs={'class': 'form-control', "id":"first-name-icon", "placeholder":"Nombre d'exemplaire"}),
        }



