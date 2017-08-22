from django.shortcuts import render, HttpResponse
from django.views import View
import hashlib, hmac
from django.conf import settings


# Create your views here.
class Cookie(View):

    def make_secure_val(self, cookie_str):
        # hash = (hashlib.md5(cookie_str.encode('utf-8'))).hexdigest()
        hash = hmac.new(settings.SECRET_KEY.encode('utf-8'), cookie_str.encode('utf-8'), 'md5').hexdigest()
        return '{},{}'.format(cookie_str, hash)

    def check_secure_val(self, cookie_hash):
        try:
            fig, _ = cookie_hash.split(',')
        except (ValueError, AttributeError):
            return None
        est_cookie = self.make_secure_val(fig)
        if est_cookie == cookie_hash:
            return fig
        else:
            return None



    def get(self, request):

        visits = 0

        visits_str = request.COOKIES.get('visits')

        secure_val = self.check_secure_val(visits_str)

        if secure_val:
            visits = int(secure_val)

        visits += 1


        if visits >= 100000:
            response = HttpResponse("You are the best ever! You've been here {} times".format(visits))
        else:
            response = HttpResponse("You've been here {} times".format(visits))


        response.__setitem__('Set-Cookie', '{}={}'.format('visits', self.make_secure_val(str(visits))))

        return response


