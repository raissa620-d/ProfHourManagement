from django.db import models

# Modèle Matière
class Matiere(models.Model):
    libelle = models.CharField(max_length=100)
    volume_horaire = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.libelle

# Modèle Enseignant
class Enseignant(models.Model):
    matricule = models.CharField(max_length=20, null=True, blank=True)
    nom = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    grade = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True, default="default@example.com")
    filiere = models.CharField(max_length=100)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name="enseignants")

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.grade} ({self.matiere.libelle})"

# Modèle Cours
class Cours(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name="cours")
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name="cours")
    date_seance = models.DateField(null=True, blank=True)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

    def __str__(self):
        return f"{self.matiere.libelle} - {self.enseignant.nom} {self.enseignant.prenom} ({self.date_seance}, {self.heure_debut}-{self.heure_fin})"

# Modèle Devoir
class Devoir(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name="devoirs")  # Ajout du related_name
    date_prevue = models.DateField()
    statut = models.CharField(max_length=20, default="Prévu")

    def __str__(self):
        return f"Devoir {self.cours.matiere.libelle} ({self.date_prevue})"
