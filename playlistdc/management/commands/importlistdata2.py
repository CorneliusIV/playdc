from django.core.management.base import BaseCommand
from datetime import datetime
from bs4 import BeautifulSoup
import urllib.request

from playlistdc.models import Artist, Show


class Command(BaseCommand):
    args = ''
    help = 'Scrape target site for upcoming artist.'

    def handle(self, *args, **options):
        r = urllib.request.urlopen('http://www.930.com/').read()
        soup = BeautifulSoup(r, 'html.parser')
        # soup = BeautifulSoup(open("test.html"))
        show_list = soup.find(id='upcoming-listview')
        for event in show_list.select('div.list-view-item'):
            title = ""
            event_details = event.find(class_='list-view-details vevent')
            for headliner in event_details.find_all(class_='headliners summary'):
                artist_name = headliner.a.string
                artist, created = Artist.objects.update_or_create(
                    name=artist_name)
            for topline in event.find_all(class_='topline-info'):
                topline_desc = topline.string
                if topline_desc:
                    title += topline_desc
            if artist_name:
                    title += ' ' + artist_name
            for description in event.find_all(class_='supports description'):
                description_desc = description.a.string
                if description_desc:
                    title += ' ' + description_desc
            print(title)

            for date in event.select('div.list-view-details.vevent > h2.dates'):
                date = date.text

                if date:
                    date = datetime.strptime(date + ' 2017', '%a %d %b %Y')
                    Show.objects.update_or_create(
                        title=title,
                        artist=artist,
                        date=date)
