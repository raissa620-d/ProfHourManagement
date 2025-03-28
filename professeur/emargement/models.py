from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta

# Modèle Filiere pour gérer les filières
class Filiere(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom

# Modèle Enseignant
class Enseignant(models.Model):
    nom = models.CharField(max_length=100, default="Inconnu")
    prenom = models.CharField(max_length=100, default="Inconnu")
    matricule = models.CharField(max_length=50, unique=True, default="MATRICULE_INCONNU")
    email = models.EmailField(unique=True)
    grade = models.CharField(max_length=50, default="Non spécifié")
    contact = models.CharField(max_length=20, default="0000000000")
    # Relation ManyToMany avec Matiere via le modèle Enseignement
    matieres = models.ManyToManyField('Matiere', through='Enseignement')

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.matricule}"

# Modèle Matiere
class Matiere(models.Model):
    nom = models.CharField(max_length=100, default="Inconnu")
    volume_horaire_total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nom

# Modèle de relation entre Enseignant, Matiere et Filiere
class Enseignement(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, default=1)
    horaire = models.CharField(max_length=100)  # Exemple : "Lundi 7h-9h"

    def __str__(self):
        return f"{self.enseignant} - {self.matiere} - {self.filiere} ({self.horaire})"

# Modèle EmargementAvantCours
class EmargementAvantCours(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    heure_debut = models.TimeField()

    class Meta:
        unique_together = ('enseignant', 'matiere', 'filiere', 'date')

    def __str__(self):
        return f"{self.enseignant} - {self.matiere} - {self.filiere} (Début : {self.heure_debut})"

# Modèle EmargementApresCours
class EmargementApresCours(models.Model):
    emargement_avant = models.OneToOneField(EmargementAvantCours, on_delete=models.CASCADE)
    heure_fin = models.TimeField()

    def duree_seance(self):
        debut = timedelta(hours=self.emargement_avant.heure_debut.hour, minutes=self.emargement_avant.heure_debut.minute)
        fin = timedelta(hours=self.heure_fin.hour, minutes=self.heure_fin.minute)
        return (fin - debut).total_seconds() / 3600

    def __str__(self):
        return f"{self.emargement_avant.enseignant} - {self.emargement_avant.matiere} - Fin : {self.heure_fin}"

# Modèle SuiviVolumeHoraire
class SuiviVolumeHoraire(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, default=1)
    volume_horaire_restant = models.FloatField(default=0)

    def __str__(self):
        return f"Suivi: {self.enseignant} - {self.matiere} - {self.filiere} - Restant: {self.volume_horaire_restant}h"

# Signal pour mettre à jour le volume horaire après un émargement après cours
@receiver(post_save, sender=EmargementApresCours)
def mettre_a_jour_volume_horaire(sender, instance, **kwargs):
    enseignant = instance.emargement_avant.enseignant
    matiere = instance.emargement_avant.matiere
    filiere = instance.emargement_avant.filiere
    duree = instance.duree_seance()

    suivi, created = SuiviVolumeHoraire.objects.get_or_create(
        enseignant=enseignant, matiere=matiere, filiere=filiere,
        defaults={'volume_horaire_restant': matiere.volume_horaire_total}
    )

    if suivi.volume_horaire_restant > 0:
        suivi.volume_horaire_restant = max(suivi.volume_horaire_restant - duree, 0)
        suivi.save()
    # La création automatique de devoirs a été supprimée

# Modèle Devoir (programmation manuelle par l'administration)
class Devoir(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, default=1)
    date = models.DateField()

    def __str__(self):
        return f"Devoir: {self.matiere} - {self.filiere} ({self.date})"
