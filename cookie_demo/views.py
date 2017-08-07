from django.shortcuts import render, HttpResponse
from django.views import View
import hashlib

# Create your views here.
class Cookie(View):

    def make_secure_val(self, cookie_str):
        hash = (hashlib.md5(cookie_str.encode('utf-8'))).hexdigest()
        return '{},{}'.format(cookie_str, hash)


    def get(self, request):


        visits = 0


        visits_str = request.COOKIES.get('visits')

        if visits_str:
            visits = int(visits_str) + 1


        if visits >= 100000:
            response = HttpResponse("You are the best ever! You've been here {} times".format(visits))
        else:
            response = HttpResponse("You've been here {} times".format(visits))


        response.__setitem__('Set-Cookie', self.make_secure_val(str(visits)))

        return response
