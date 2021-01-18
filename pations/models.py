from django.db import models

# Create your models here.

from django.urls import reverse


class Diagnos(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Patient(models.Model):
    surname = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    adress = models.CharField(max_length=225)
    phonenumber = models.CharField(max_length=225)
    discrict = models.CharField(max_length=225)
    diagnos = models.ForeignKey(Diagnos, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('patient_detail', self.id)

    def __str__(self):
        return self.name
