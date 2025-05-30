# Generated by Django 5.1.6 on 2025-03-13 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emargement', '0002_cours_heure_cumulee'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='heure_restante',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cours',
            name='heure_cumulee',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='matiere',
            name='volume_horaire',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
