from django.shortcuts import render, redirect
from django.views import View
from .models import Art


class AsciiView(View):


    def arts(self):
        return list(Art.objects.all().order_by('-created'))

    def get(self, request):
        return render(request, 'ascii_chan/ascii_chan.html', {'arts': self.arts()})

    def post(self, request):
        title = request.POST.get('title')
        art = request.POST.get('art')
        if title and art:
            Art.objects.create(title=title, art=art)
            return redirect('/ascii_chan/')
        else:
            return render(request, 'ascii_chan/ascii_chan.html', {'error':'We need both title and some text.', 'art': art, 'title': title, 'arts': self.arts()})