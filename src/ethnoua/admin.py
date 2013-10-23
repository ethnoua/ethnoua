from django.contrib import admin

from .models import Region, City, Song


admin.site.register(Region)
admin.site.register(City)
admin.site.register(Song)