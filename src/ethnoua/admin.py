from django.contrib import admin

from .models import (Region, City, Location, Song, Commons,
    Clothes, Buildings, BuildingType, Photo)


class SongAdmin(admin.ModelAdmin):
    pass


class BuildingTypeAdmin(admin.ModelAdmin):
    pass


class BuildingsAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)


admin.site.register(Buildings, BuildingsAdmin)
admin.site.register(BuildingType, BuildingTypeAdmin)

admin.site.register(Location, LocationAdmin)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Commons)
admin.site.register(Photo)
admin.site.register(Song, SongAdmin)