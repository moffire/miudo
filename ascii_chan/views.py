from django.shortcuts import render, redirect
from django.views import View
from .models import Art
import urllib, json
from random import uniform
from django.conf import settings
# google-maps API AIzaSyAaBupiwy7RA2R8ARNfAcsoMQ3Baopq2_I

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
        all_posts = Art.objects.all().order_by('-created')
        coords = []
        for post in all_posts:
            if post.lat and post.lon:
                coords.append((post.lat, post.lon))
        return all_posts

    def get(self, request):
        ip = '208.80.152.201'
        coords = self.getcoords(ip)
        return render(request, 'ascii_chan/ascii_chan.html', {'arts': self.arts(), 'coords': coords})


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
            return redirect('/ascii_chan/')
        else:
            return render(request, 'ascii_chan/ascii_chan.html', {'error':'We need both title and some text.', 'art': art, 'title': title, 'arts': self.arts()})