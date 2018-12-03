from django.contrib import admin
from apartments.models import (Apartment, ApartmentImages,
                               Customer, Reservation)

# Register your models here.
admin.site.register(Apartment)
admin.site.register(ApartmentImages)
admin.site.register(Customer)
admin.site.register(Reservation)
