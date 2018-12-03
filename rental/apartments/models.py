from django.db import models
from django.contrib.auth.models import User


class Apartment(models.Model):

    class Meta:
        db_table = 'apartment'

    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name


class ApartmentImages(models.Model):

    class Meta:
        db_table = 'apartment_images'

    apartment = models.ForeignKey(
        to=Apartment, related_name='images', on_delete=models.CASCADE)


class Reservation(models.Model):

    class Meta:
        db_table = 'apartment_reservations'

    apartment = models.ForeignKey(
        to=Apartment, related_name='reservations', on_delete=models.CASCADE)


class Customer(models.Model):

    class Meta:
        db_table = 'customer'

    # TODO: Add language choices
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
