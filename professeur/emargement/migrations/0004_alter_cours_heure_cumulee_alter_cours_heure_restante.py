# Generated by Django 5.1.6 on 2025-03-13 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emargement', '0003_cours_heure_restante_alter_cours_heure_cumulee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='heure_cumulee',
            field=models.FloatField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='cours',
            name='heure_restante',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
    ]
