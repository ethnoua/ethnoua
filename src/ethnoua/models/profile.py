import datetime

from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.user.username

    class Meta:
        db_table = 'profiles'
        app_label = 'ethnoua'
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
