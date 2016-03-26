from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Artist(models.Model):
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,)
    spotify_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,)

    def __str__(self):
            return self.name

    class Meta:
        verbose_name = _('Name')


class Venue(models.Model):
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,)
    location = models.CharField(
        max_length=255,
        null=True,
        blank=True,)


class Show(models.Model):
    title = models.TextField(
        null=True,
        blank=True,)
    artist = models.ForeignKey(Artist)
    date = models.DateTimeField(
        blank=True,
        null=True)
    venue = models.ForeignKey(
        Venue,
        blank=True,
        null=True)


class Song(models.Model):
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,)
    artist = models.ForeignKey(Artist)
    album = models.CharField(
        max_length=255,
        null=True,
        blank=True,)
    spotify_track_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,)
