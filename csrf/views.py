from django.shortcuts import render
from django.views import View
import getpass


class CSRF(View):

    user = getpass.getuser()

    def get(self, request):
        return render(request, 'csrf/index.html', {'user': self.user})


def reward(request):

    ALLOWED_CSRF = ['12345']

    csrf = request.POST.get('csrf')

    if request.POST:
        if csrf in ALLOWED_CSRF:
            q = request.POST.get('q')
            return render(request, 'csrf/testform.html', {'q': q})
        else:
            return render(request, 'csrf/testform.html', {'error': 'Oops!!'})