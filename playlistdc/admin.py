from django.contrib import admin
from .models import Artist, Venue, Show, Song


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
