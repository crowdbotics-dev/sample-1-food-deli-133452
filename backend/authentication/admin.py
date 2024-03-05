from django.contrib import admin
from .models import Customer, Driver, RestaurantPartner

admin.site.register(Driver)
admin.site.register(RestaurantPartner)
admin.site.register(Customer)

# Register your models here.
