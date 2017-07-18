from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render
import psycopg2

class FormView(View):

    def get(self, request):
        return render(request, 'home/shopping_list.html')


    def post(self, request):
        city = request.POST.get('city')
        try:
            conn = psycopg2.connect(dbname='world', user='www-data', password='password', port='5432')
        except psycopg2.OperationalError:
            print("Unable to connect to db!")
            exit()

        # Define a cursor to work with.
        cur = conn.cursor()

        # Execute a query
        SQL = "select * from city where name = (%s);"
        data = (city,)
        cur.execute(SQL, data)

        # We need a list to put the results in.
        rows = cur.fetchall()

        return render(request, 'home/shopping_list.html', context={'rows': rows})

class ThanksHandler(View):

    def get(self, request, id):
        return HttpResponse('Thanks! That is a totally valid date for id:{name}'.format(name = id))