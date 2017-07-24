from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=200, null=False)
    text = models.TextField(null=False)
    post_publish_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title

class Comment(models.Model):

    post = models.ForeignKey(Post)
    comment_text = models.TextField()
    comment_publish_date = models.DateTimeField(auto_created=True)