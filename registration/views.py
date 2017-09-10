from django.shortcuts import render, redirect
from django.views import View
import re, hashlib, binascii, hmac
from registration.models import User
from django.conf import settings

class Cookie_Hash_Mixin():


    def make_cookie_hash(self, id_cookie):

        hash = hmac.new(settings.SECRET_KEY.encode('utf-8'), str(id_cookie).encode('utf-8'), 'md5').hexdigest()
        return '{},{}'.format(id_cookie, hash)
        # return id_cookie, hash

    def check_cookie_hash(self, cookie_hash):

        # try:
        id , _ = cookie_hash.split(',')
        # except (ValueError, AttributeError):
        #     return None

        # est_cookie = self.make_cookie_hash(id)
        # new_hash = est_cookie.split(',')
        new_hash = self.make_cookie_hash(id)

        if new_hash == cookie_hash:
            return True
        else:
            return None

class MainForm(Cookie_Hash_Mixin, View):

    error_form = 'You should to fill all fields'
    error_password = 'Passwords doesnt match'
    user_exists = 'This user is already exists'

    def get(self, request):

        return render(request, 'registration/registration.html')

    def make_password_hash(self, pw):

        salt = 'salt'
        hash_byte = hashlib.pbkdf2_hmac('sha256', pw.encode('utf-8'), salt.encode('utf-8'), 100000)
        hash_string = binascii.hexlify(hash_byte).decode()
        return ','.join([hash_string, salt])


    def check_name_email_errors(self, name, email):

        user_re = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
        email_re = re.compile('^[\S]+@[\S]+.[\S]+$')

        if user_re.match(name) and email_re.match(email):
            return {'name': user_re, 'email': email_re}

    def check_passwords(self, password, confirm_password):

        if len(password) and len(confirm_password) >= 1:
            if password == confirm_password:
                return {'password': password, 'confirm_password': confirm_password}

    def post(self, request):

        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        hashed_password = self.make_password_hash(password)


        validate_name_email = self.check_name_email_errors(name, email)
        validate_password = self.check_passwords(password, confirm_password)

        if validate_name_email and validate_password is not None:
            response = redirect('/welcome/')

            if User.objects.filter(name = name).exists():
                return render(request, 'registration/registration.html', {'user_exists': self.user_exists, 'name': name, 'email': email})


            else:
                User.objects.create(name = name, email = email, password = hashed_password, confirm_password = self.make_password_hash(confirm_password))
                new_user_id = User.objects.get(name = name).id
                response.set_cookie('id', self.make_cookie_hash(new_user_id))
                return response

        elif validate_name_email is None:
            return render(request, 'registration/registration.html', {'error_form': self.error_form, 'name': name, 'email': email})

        elif validate_password is None:
            return render(request, 'registration/registration.html', {'error_password': self.error_password, 'name': name, 'email': email})

class LoginForm(Cookie_Hash_Mixin, View):


    def get(self, request):

        id, _ = request.COOKIES.get('id').split(',')
        user_name = User.objects.get(id = id).name
        if Cookie_Hash_Mixin.check_cookie_hash(self, request.COOKIES.get('id')):
            return render(request, 'registration/welcome.html', {'name': user_name})
        else:
            render(request, 'registration/registration.html')