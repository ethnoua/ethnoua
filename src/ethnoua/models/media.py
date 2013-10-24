import datetime

from django.db import models


class BaseMedia(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(
        auto_now_add=True, default=datetime.datetime.now
    )
    updated = models.DateTimeField(default=datetime.datetime.now)
    is_published = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class Song(BaseMedia):
    file = models.FileField(upload_to="m/songs")
    author = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    notes_file = models.FileField(upload_to="m/notes", null=True)
    lyrics = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'songs'
        app_label = 'ethnoua'
        verbose_name = 'song'
        verbose_name_plural = 'songs'


class Photo(BaseMedia):
    file = models.FileField(upload_to="m/photos")

    class Meta:
        db_table = 'photos'
        app_label = 'ethnoua'
        verbose_name = 'photo'
        verbose_name_plural = 'photos'


class Clothes(BaseMedia):
    file = models.FileField(upload_to="m/clothes")

    class Meta:
        db_table = 'clothes'
        app_label = 'ethnoua'
        verbose_name = 'clothes'
        verbose_name_plural = 'clothes'


class Commons(BaseMedia):
    file = models.FileField(upload_to="m/commons")

    class Meta:
        db_table = 'commons'
        app_label = 'ethnoua'
        verbose_name = 'common'
        verbose_name_plural = 'commons'


class BuildingType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'building_types'
        app_label = 'ethnoua'
        verbose_name = 'building type'
        verbose_name_plural = 'building types'


class Buildings(BaseMedia):
    file = models.FileField(upload_to='m/buildings')
    type = models.ForeignKey(BuildingType, null=True)

    class Meta:
        db_table = 'bildings'
        app_label = 'ethnoua'
        verbose_name = 'buiding'
        verbose_name_plural = 'buildings'