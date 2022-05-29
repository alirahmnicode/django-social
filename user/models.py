from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=11)
    is_active_account = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["phone_number"]