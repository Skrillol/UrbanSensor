from django.db import models

# Create your models here.
class CustomUser(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=13, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    dateBorn = models.DateField()
    dateCreated = models.DateField(auto_now_add=True)
    dateEdited = models.DateField(auto_now=True)
    def __str__(self):
        testo = "{0} ({1})"
        return testo.format(self.id, self.name, self.lastname, self.rut, self.email)
    
class CuestomRols(models.Model):
    id = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=50)  # Nuevo campo
    Departement = models.CharField(max_length=100)  # Nuevo campo
    addressDepartement = models.CharField(max_length=255)  # Nuevo campo
    is_admin = models.BooleanField(default=False)  # Nuevo campo para asignar rol de administrador
    is_active = models.BooleanField(default=True)
    dateCreated = models.DateField(auto_now_add=True)
    dateEdited = models.DateField(auto_now=True)
    ForeignKey = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        testo = "{0} ({1})"
        return testo.format(self.id, self.rol, self.Departement, self.is_active, self.is_admin)
    
class UsersPassword(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=50)
    dateCreated = models.DateField(auto_now_add=True)
    dateEdited = models.DateField(auto_now=True)
    ForeignKey = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        testo = "{0} ({1})"
        return testo.format(self.id, self.password)