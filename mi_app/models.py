from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField(default=True)
    nacimiento = models.DateField(default= True)

 
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    entregado = models.BooleanField()
    fechadeentrega = models.DateField()
   
