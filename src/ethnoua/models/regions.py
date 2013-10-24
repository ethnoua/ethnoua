import datetime

from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(
        auto_now_add=True, default=datetime.datetime.now
    )
    updated = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'regions'
        app_label = 'ethnoua'


class City(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'cities'
        app_label = 'ethnoua'
        verbose_name = 'city'
        verbose_name_plural = 'cities'


class Location(models.Model):
    region = models.ForeignKey(Region, null=True)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(
        auto_now_add=True, default=datetime.datetime.now
    )
    updated = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'locations'
        app_label = 'ethnoua'
        verbose_name = 'location'
        verbose_name_plural = 'locations'