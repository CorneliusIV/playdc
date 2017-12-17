import pprint
import spotipy
import spotipy.util as util

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    args = ''
    help = 'Create Playlist'

    def handle(self, *args, **options):
        username = 'koolexposure'
        scope = 'playlist-modify-public'

        token = util.prompt_for_user_token(username, scope)
        if token:
            sp = spotipy.Spotify(auth=token)
            sp.trace = False
            playlists = sp.user_playlist_create(username, "Playlist DC")
            pprint.pprint(playlists)
        else:
            print("Can't get token for", username)
