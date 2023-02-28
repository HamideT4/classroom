from django.contrib import admin
from .models import*

@admin.register(Etudiant)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'genre','telephone', 'email', )
    ordering = ('nom', )
    search_fields =  ('nom', )

@admin.register(Groupe)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('nom', )
    ordering = ('nom', )
    search_fields =  ('nom', )

@admin.register(Commande)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('menu','quantite', )
    ordering = ('menu', )
    search_fields =  ('menu', )