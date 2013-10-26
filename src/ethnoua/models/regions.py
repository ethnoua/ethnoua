import datetime

from django.contrib.gis.db import models


class Region(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(
        auto_now_add=True, default=datetime.datetime.now
    )
    updated = models.DateTimeField(default=datetime.datetime.now)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'regions'
        app_label = 'ethnoua'


class City(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    name = models.CharField(max_length=255)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'cities'
        app_label = 'ethnoua'
        verbose_name = 'city'
        verbose_name_plural = 'cities'


class Location(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    region = models.ForeignKey(Region, null=True)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(
        auto_now_add=True, default=datetime.datetime.now
    )
    updated = models.DateTimeField(default=datetime.datetime.now)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'locations'
        app_label = 'ethnoua'
        verbose_name = 'location'
        verbose_name_plural = 'locations'