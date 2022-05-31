from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    description = models.TextField()
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes')
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tags')
    label = models.CharField(max_length=100)