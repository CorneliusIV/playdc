from django.core.management.base import BaseCommand
import spotipy

from playlistdc.models import Artist


class Command(BaseCommand):
    args = ''
    help = 'Grab IDs from Spotify'

    def handle(self, *args, **options):
        spotify = spotipy.Spotify()
        artists = Artist.objects.all()
        for artist in artists:
            sp_artist = spotify.search(q=artist, type='artist')
            if sp_artist:
                for t in (sp_artist['artists']['items'])[:1]:
                    print(artist.name)
                    print (t['uri'])
                    artist.spotify_id = t['uri']
                    artist.save()