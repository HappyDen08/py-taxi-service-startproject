from django.contrib.auth.models import AbstractUser
from django.db import models
from taxi_service import settings


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)
    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"


class Manufacturer(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE, unique=True)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Cars")

    def __str__(self) -> str:
        return str(self.model)
