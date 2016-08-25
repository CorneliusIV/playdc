import pprint
import datetime
import spotipy
import spotipy.util as util

from django.core.management.base import BaseCommand

from playlistdc.models import Song, Show


class Command(BaseCommand):
    args = ''
    help = 'Grab IDs from Spotify'

    def handle(self, *args, **options):
        username = 'koolexposure'
        scope = 'playlist-modify-public'
        playlist_id = 'spotify:user:koolexposure:playlist:2STrNLJzvaHGWgU2SIwYZa'

        token = util.prompt_for_user_token(username, scope)
        if token:
            sp = spotipy.Spotify(auth=token)
            sp.trace = False

            all_tracks = Song.objects.values_list(
                'spotify_track_id', flat=True)
            sp.user_playlist_remove_all_occurrences_of_tracks(
                username, playlist_id, all_tracks)

            track_ids = set()
            for show in Show.objects.filter(
                    date__gt=datetime.datetime.now()).select_related('artist'):
                spotify_track = show.artist.song_set.values_list(
                    'spotify_track_id', flat=True).first()
                if spotify_track is not None:
                    track_ids.add(spotify_track)
            sp.user_playlist_add_tracks(username, playlist_id, track_ids)
        else:
            print("Can't get token for", username)
