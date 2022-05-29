from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=11)
    is_active_account = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["phone_number"]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, upload_to='profile image')
    baio = models.TextField()
    follower = models.ManyToManyField(User, related_name='followers')
    following = models.ManyToManyField(User, related_name='following')
    created = models.DateTimeField(auto_now_add=True)

