"""simple_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from home.views import FormView, ThanksHandler
from FizzBuzz.views import FizzBuzz
from ascii_chan.views import AsciiView
from blog.views import Blog, New_Post
from cookie_demo.views import Cookie




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^form/$', FormView.as_view()),
    url(r'^thanks/(?P<id>\d+)/$', ThanksHandler.as_view()),
    url(r'^fizzbuzz/$', FizzBuzz.as_view()),
    url(r'^ascii_chan/$', AsciiView.as_view()),
    url(r'^blog/$', Blog.as_view()),
    url(r'^blog/(?P<id>\d+)/$', Blog.post_details),
    url(r'^new_post/$', New_Post.as_view()),
    url(r'^cookie/$', Cookie.as_view()),
]
