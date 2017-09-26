from django.shortcuts import render, redirect
from django.views import View
from .models import Art
import urllib, json
from random import uniform
from django.conf import settings
import time
from collections import deque
# google-maps API AIzaSyDdbE5O_wI9RyFNYzii-8ARBIrcqVXwyZ8

class AsciiView(View):

    cache = {}

    def get_arts(self, art=False):
        KEY = 'arts'
        # if KEY in self.cache:
        #     return self.cache[KEY]
        # else:
        #     all_posts = Art.objects.all().order_by('-created')
        #     time.sleep(3)
        #     self.cache[KEY] = all_posts
        #     print('Db query')
        #     return all_posts
        if not KEY in self.cache:
            print('Db query')
            arts = Art.objects.all()
            self.cache[KEY] = arts
            return arts

        if KEY in self.cache and art:
            arts = self.cache[KEY]
            deque_arts = deque(arts)
            deque_arts.appendleft(art)
            self.cache[KEY] = deque_arts
            return deque_arts

        else:
            return self.cache[KEY]

    def getcoords(self, ip):
        if settings.DEBUG:
            lat = self.get_random_lat()
            lon = self.get_random_lon()
            return lat, lon
        else:
            response = (urllib.request.urlopen('http://ip-api.com/json/'+ ip)).read().decode()
            json_content = json.loads(response)
            return json_content['lat'], json_content['lon']

    def arts(self):
        # all_posts = Art.objects.all().order_by('-created')
        all_posts = self.get_arts()
        coords = []
        for post in all_posts:
            if post.lat and post.lon:
                coords.append((post.lat, post.lon))
        return all_posts

    def prepare_points(self, arts):

        coords = ''

        for art in arts:
            if art.lat and art.lon:
                coords += str(art.lat) + ',' + str(art.lon) + '|'

        coords_without_last_pipe = coords[:-1]
        google_row = 'https://maps.googleapis.com/maps/api/staticmap?size=400x400&maptype=roadmap&markers={}&key=AIzaSyDdbE5O_wI9RyFNYzii-8ARBIrcqVXwyZ8'.format(coords_without_last_pipe)
        return google_row

    def get(self, request):
        arts = self.get_arts()
        return render(request, 'ascii_chan/ascii_chan.html', {'arts': arts, 'map_url': self.prepare_points(arts)})


    def get_random_lon(self):
        return uniform(-180, 180)

    def get_random_lat(self):
        return uniform(-90, 90)


    def post(self, request):
        title = request.POST.get('title')
        art = request.POST.get('art')
        ip = '208.80.152.201'
        lat, lon = self.getcoords(ip)
        if title and art:
            new_art = Art.objects.create(title = title, art = art, lat = lat, lon = lon)
            self.get_arts(new_art)
            return redirect('/ascii_chan/')
        else:
            return render(request, 'ascii_chan/ascii_chan.html', {'error':'We need both title and some text.', 'art': art, 'title': title, 'arts': self.arts()})

