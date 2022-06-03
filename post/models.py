from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(blank=True)
    tags = TaggableManager(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title} - {self.user.username}'
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
