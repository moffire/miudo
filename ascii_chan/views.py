from django.shortcuts import render, redirect
from django.views import View
from .models import Art
import urllib, json
from random import uniform
from django.conf import settings
import time
# google-maps API AIzaSyDdbE5O_wI9RyFNYzii-8ARBIrcqVXwyZ8


cache = {}

def get_arts(update=False):
    KEY = 'arts'
    if (KEY in cache) and (update == False):
        return cache[KEY]
    else:
        all_posts = Art.objects.all().order_by('-created')
        time.sleep(3)
        cache[KEY] = all_posts
        print('Db query')
        return all_posts

class AsciiView(View):

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
        all_posts = get_arts()
        coords = []
        for post in all_posts:
            if post.lat and post.lon:
                coords.append((post.lat, post.lon))
        return all_posts

    def prepare_points(self, arts):

        coords = ''

        for art in arts:
            if art.lat and art.lon:
                coords += art.lat + ',' + art.lon + '|'

        coords_without_last_pipe = coords[:-1]
        google_row = 'https://maps.googleapis.com/maps/api/staticmap?size=400x400&maptype=roadmap&markers={}&key=AIzaSyDdbE5O_wI9RyFNYzii-8ARBIrcqVXwyZ8'.format(coords_without_last_pipe)
        return google_row

    def get(self, request):
        arts = Art.objects.all()
        return render(request, 'ascii_chan/ascii_chan.html', {'arts': self.arts(), 'map_url': self.prepare_points(arts)})


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
            Art.objects.create(title = title, art = art, lat = lat, lon = lon)
            get_arts(update=True)
            return redirect('/ascii_chan/')
        else:
            return render(request, 'ascii_chan/ascii_chan.html', {'error':'We need both title and some text.', 'art': art, 'title': title, 'arts': self.arts()})

