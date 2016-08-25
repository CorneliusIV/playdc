from django.core.management.base import BaseCommand
import spotipy

from playlistdc.models import Artist, Song


class Command(BaseCommand):
    args = ''
    help = 'Grab IDs from Spotify'

    def handle(self, *args, **options):
        spotify = spotipy.Spotify()
        artists = Artist.objects.all()
        for artist in artists:
            if artist.spotify_id:
                sp_track = spotify.artist_top_tracks(artist.spotify_id)
                if sp_track:
                    for t in (sp_track['tracks'])[:1]:
                        print(artist.name)
                        print(t['name'])
                        print(t['uri'])
                        Song.objects.update_or_create(
                            title=t['name'],
                            artist=artist,
                            spotify_track_id=t['uri'],
                            preview=t['preview_url']
                        )
                        # artist.spotify_id = t['uri']
                        # artist.save()
