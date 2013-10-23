from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=255)

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