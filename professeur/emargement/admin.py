
from django.contrib import admin
from .models import Matiere, Enseignant, Cours, Devoir

@admin.register(Enseignant)
class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'matricule', 'grade', 'email', 'filiere', 'matiere')
    search_fields = ('nom', 'prenom', 'matricule', 'email')

@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'volume_horaire')

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ('matiere', 'enseignant', 'date_seance', 'heure_debut', 'heure_fin')
    list_filter = ('matiere', 'enseignant')

@admin.register(Devoir)
class DevoirAdmin(admin.ModelAdmin):
    list_display = ('cours', 'date_prevue', 'statut')
