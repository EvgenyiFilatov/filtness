from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    birthday = models.DateField(
        "Дата рождения", null=True, blank=True
        )
