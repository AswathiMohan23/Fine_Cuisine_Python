from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class UserModel(AbstractUser):
    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = "user"
