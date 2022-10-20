from django.contrib import admin
from .models import *


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'site', 'email', 'phone',
                    'street', 'city', 'state', 'lat', 'lng')


admin.site.register(Restaurant, RestaurantAdmin)
