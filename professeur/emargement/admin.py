from django.contrib import admin
from .models import (
    Enseignant, Matiere, Filiere, Enseignement,
    EmargementAvantCours, EmargementApresCours, SuiviVolumeHoraire, Devoir
)

@admin.register(Enseignant)
class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'nom', 'prenom', 'email', 'grade', 'contact')
    search_fields = ('nom', 'prenom', 'matricule', 'email')
    list_filter = ('grade',)

@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ('nom', 'volume_horaire_total')
    search_fields = ('nom',)

@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    search_fields = ('nom',)

@admin.register(Enseignement)
class EnseignementAdmin(admin.ModelAdmin):
    list_display = ('enseignant', 'matiere', 'filiere', 'horaire')
    list_filter = ('enseignant', 'matiere', 'filiere')
    search_fields = ('enseignant__nom', 'matiere__nom', 'filiere__nom')

@admin.register(EmargementAvantCours)
class EmargementAvantCoursAdmin(admin.ModelAdmin):
    list_display = ('enseignant', 'matiere', 'filiere', 'date', 'heure_debut')
    list_filter = ('date', 'filiere', 'matiere', 'enseignant')
    search_fields = ('enseignant__nom', 'matiere__nom', 'filiere__nom')

@admin.register(EmargementApresCours)
class EmargementApresCoursAdmin(admin.ModelAdmin):
    list_display = ('emargement_avant', 'heure_fin', 'duree_seance')
    list_filter = ('emargement_avant__date',)
    search_fields = ('emargement_avant__enseignant__nom', 'emargement_avant__matiere__nom')

@admin.register(SuiviVolumeHoraire)
class SuiviVolumeHoraireAdmin(admin.ModelAdmin):
    list_display = ('enseignant', 'matiere', 'filiere', 'volume_horaire_restant')
    list_filter = ('matiere', 'filiere', 'enseignant')
    search_fields = ('enseignant__nom', 'matiere__nom', 'filiere__nom')

@admin.register(Devoir)
class DevoirAdmin(admin.ModelAdmin):
    list_display = ('matiere', 'filiere', 'date')
    list_filter = ('date', 'matiere', 'filiere')
    search_fields = ('matiere__nom', 'filiere__nom')
