from django.core.management.base import BaseCommand

from bs4 import BeautifulSoup
import urllib

from playlistdc.models import Artist, Venue


class Command(BaseCommand):
    args = ''
    help = 'Scrape target site for upcoming artist.'

    def handle(self, *args, **options):
        r = urllib.urlopen('http://www.930.com/').read()
        soup = BeautifulSoup(r)
        for headliner in soup.find_all(class_='headliners summary'):
            artist_name = headliner.a.string
            Artist.objects.update_or_create(
                name=artist_name)
