from django import forms
#from django.forms import ModelForm
from .models import Etudiant, Groupe, Commande

class EtudiantForm(forms.ModelForm):
	class Meta:
		model = Etudiant
		fields = [ 'nom', 'prenom', 'genre', 'email',  'telephone',  'groupe', 'photo',]

		labels = {
			'nom': 'Nom', 
			'prenom': 'Prenom',       
			'genre': 'Genre ', 
			'email': 'Email',
			'telephone': 'Telephone', 
			'groupe': 'Groupe',  
			'photo': 'Selectionner une photo',  
		}

		widgets = {
			'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le nom',}), 
			'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le prenom',}), 
			'genre': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Genre',}), 
			'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email',}), 
			'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telephone',}),
			'groupe': forms.Select(attrs={'class': 'form-select', 'placeholder': 'adresse',}),
			#'photo': forms.ImageField()
		}

class GroupeForm(forms.ModelForm):
	class Meta:
		model = Groupe
		fields = [ 'nom',]

		labels = {
			'nom': 'Nom',
		}

		widgets = {
			'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le nom du groupe',}),
		}

class CommandeForm(forms.ModelForm):
	class Meta:
		model = Commande
		fields = [ 'menu', 'quantite', 'groupe', 'etudiant',]

		labels = {
			'menu': 'Menu', 
			'groupe': 'Groupe en service ',
			'quantite': 'Quantite',        
			'etudiant': 'Nom de l\'etudiant',  
		}

		widgets = {
			'menu': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Menu',}), 
			#'quantite': forms.IntegerField(attrs={'class': 'form-control', 'placeholder': 'Quantité',}), 
			'groupe': forms.Select(attrs={'class': 'form-select', 'placeholder': 'adresse',}),
			#'etudiant': forms.SelectMultiple(attrs={'class': 'form-select', 'placeholder': 'Choisir l\'etudiant',}), 
		}

