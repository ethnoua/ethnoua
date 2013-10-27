import datetime

from django.contrib.gis.db import models


class LandingPageSubscription(models.Model):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.email

    class Meta:
        db_table = 'landingpagesubscriptions'
        app_label = 'ethnoua'
        verbose_name = 'landing page subscription'
        verbose_name_plural = 'landing page subscriptions'
