import datetime

from django.db import models


class BaseMedia(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(
        auto_now_add=True, default=datetime.datetime.now
    )
    updated = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class Song(BaseMedia):
    file = models.FileField(upload_to="m/songs")

    class Meta:
        db_table = 'songs'
        app_label = 'ethnoua'
        verbose_name = 'song'
        verbose_name_plural = 'songs'