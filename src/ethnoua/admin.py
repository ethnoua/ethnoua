from django.contrib import admin
from django.contrib.gis import admin as geo_admin

from .models import (Region, City, Location, Song, Commons,
    Clothes, Buildings, BuildingType, Photo, Profile, LandingPageSubscription)


class SongAdmin(admin.ModelAdmin):
    pass


class BuildingTypeAdmin(admin.ModelAdmin):
    pass


class BuildingsAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)


class LocationAdmin(geo_admin.GeoModelAdmin):
    list_display = ('__unicode__',)


class RegionAdmin(geo_admin.GeoModelAdmin):
    list_display = ('__unicode__',)


class CityAdmin(geo_admin.GeoModelAdmin):
    list_display = ('__unicode__',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)


class LandingPageSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(LandingPageSubscription, LandingPageSubscriptionAdmin)
admin.site.register(Buildings, BuildingsAdmin)
admin.site.register(BuildingType, BuildingTypeAdmin)

geo_admin.site.register(Location, LocationAdmin)
geo_admin.site.register(Region, RegionAdmin)
geo_admin.site.register(City, CityAdmin)
admin.site.register(Commons)
admin.site.register(Photo)
admin.site.register(Song, SongAdmin)