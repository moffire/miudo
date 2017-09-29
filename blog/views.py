from django.shortcuts import render, redirect, get_object_or_404, render_to_response, HttpResponse
from django.views import View
from .models import Post
from datetime import datetime
from django.core import serializers
import json, datetime
from collections import deque

class Blog(View):

    cache = {}

    def posts_cache(self, posts=False):
        KEY = 'posts'
        # age = datetime.time() + datetime.timedelta()

        if not KEY in self.cache:
            # time delta should be here
            print ('DB ATTACKED')
            all_posts = Post.objects.all()
            self.cache[KEY] = all_posts
            return all_posts

        if KEY in self.cache and posts:
            all_posts = self.cache[KEY]
            deque_posts = deque(all_posts)
            deque_posts.appendleft(posts)
            self.cache[KEY] = deque_posts
            return deque_posts

        else:
            return self.cache[KEY]


    def all_posts(self):
        return Post.objects.all().order_by('-post_publish_date')

    def get(self, request):
        posts = self.posts_cache()
        if not 'posts' in self.cache:
            return render(request, 'blog/post.html', {'no_posts': "Here's no posts yet"})
        else:
            return render(request, 'blog/post.html', {'posts': posts})




class New_Post(Blog, View):

    def get(self, request):
        return render(request, 'blog/new_post.html')

    def post(self, request):
        post_title = request.POST.get('title')
        post_text = request.POST.get('text')

        if post_text and post_title:
            new_post = Post.objects.create(title = post_title, text = post_text, post_publish_date = datetime.datetime.now())
            self.posts_cache(new_post)
            return render(request, 'blog/post_details.html', {'post': new_post})
        else:
            return render(request, 'blog/new_post.html', {'error': 'We need both title and some text.', 'title': post_title, 'text': post_text})

class Json_all_posts(View):

    # title
    # text
    # post_publish_date

    def get(self, request):

        all_data = serializers.serialize('python', Post.objects.all())
        all_posts = [field['fields'] for field in all_data]
        output = json.dumps(all_posts)


        return HttpResponse(output, content_type='application/json')