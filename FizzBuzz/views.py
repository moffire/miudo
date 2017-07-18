from django.shortcuts import render
from django.views import View


class FizzBuzz(View):

    def get(self, request):
        iter_number = request.GET.get('iter_number')
        iter_number = iter_number or 0
        iter_number = int(iter_number)
        loop_range = range(0, iter_number)
        return render(request, 'fizzbuzz/fizzbuzz.html', context={'loop_range':loop_range})