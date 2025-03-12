from django.db import models

# Create your models here.

from django.contrib.auth.models import User


# Modèle pour les enseignants
class Enseignant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Liaison avec le modèle User (authentification)
    matiere = models.CharField(max_length=100)
    classe_filiere = models.CharField(max_length=100)
    print()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


# Modèle pour les cours
class Cours(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    matiere = models.CharField(max_length=100)
    classe_filiere = models.CharField(max_length=100)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    statut = models.CharField(max_length=20, default='En cours')  # 'En cours', 'Terminé', etc.

    def __str__(self):
        return f"{self.matiere} - {self.classe_filiere}"


# Modèle pour les devoirs
class Devoir(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    date_prevue = models.DateField()
    statut = models.CharField(max_length=20, default='Prévu')  # 'Prévu', 'Rendu', etc.

    def __str__(self):
        return f"Devoir {self.cours.matiere} - {self.date_prevue}"
