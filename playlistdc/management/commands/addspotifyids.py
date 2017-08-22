from django.core.management.base import BaseCommand
import spotipy
import spotipy.util as util

from playlistdc.models import Artist


class Command(BaseCommand):
    args = ''
    help = 'Grab IDs from Spotify'

    def handle(self, *args, **options):
        username = 'koolexposure'
        scope = 'playlist-modify-public'
        playlist_id = 'spotify:user:koolexposure:playlist:1THotejBefoXPJoEFVKPhG'

        token = util.prompt_for_user_token(username, scope)
        if token:
            sp = spotipy.Spotify(auth=token)
            sp.trace = False
            artists = Artist.objects.all()
            for artist in artists:
                sp_artist = sp.search(q=artist, type='artist')
                if sp_artist:
                    for t in (sp_artist['artists']['items'])[:1]:
                        print(artist.name)
                        print(t['uri'])
                        artist.spotify_id = t['uri']
                        artist.save()
