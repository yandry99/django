from django.db import models

# Create your models here.
class Persona(models.Model):
       
    ci = models.CharField(primary_key=True,max_length=11,help_text="entre el carnet de identidad")
    name = models.CharField(max_length=200, help_text="Ingrese el nombre del género (p. ej. Ciencia Ficción, Poesía Francesa etc.)")
    last_name = models.CharField(max_length=200, help_text="Ingrese el apellido (p. ej. Ciencia Ficción, Poesía Francesa etc.)")

    def __str__(self):
        texto = "{0} {1} {2}"
        return texto.format(self.ci,self.name,self.last_name)
    