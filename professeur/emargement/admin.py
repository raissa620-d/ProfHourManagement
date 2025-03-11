from django.contrib import admin



from .models import Cours, Enseignant, Devoir


# Register your models here.
admin.site.register(Enseignant)
admin.site.register(Cours)
admin.site.register(Devoir)