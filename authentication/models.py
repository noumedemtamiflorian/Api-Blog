from django.db.models import *
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_verified = BooleanField(default=False)
