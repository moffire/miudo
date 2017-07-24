from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views import View
from .models import Post
from datetime import datetime

class Blog(View):

    def all_posts(self):
        return Post.objects.all().order_by('-post_publish_date')

    def get(self, request):
        if len(Post.objects.all()) == 0:
            return render(request, 'blog/post.html', {'no_posts': "Here's no posts yet"})
        else:
            return render(request, 'blog/post.html', {'posts': self.all_posts()})

    def post_details(self, id):
        post = get_object_or_404(Post, id = id)
        return render_to_response('blog/post_details.html', {'post': post})

class New_Post(View):

    def get(self, request):
        return render(request, 'blog/new_post.html')

    def post(self, request):
        post_title = request.POST.get('title')
        post_text = request.POST.get('text')

        if post_text and post_title:
            Post.objects.create(title = post_title, text = post_text, post_publish_date = datetime.now())
            return redirect('/blog/')
        else:
            return render(request, 'blog/new_post.html', {'error': 'We need both title and some text.', 'title': post_title, 'text': post_text})