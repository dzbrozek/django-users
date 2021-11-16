from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


def generate_random_number() -> int:
    import random

    return random.randint(1, 100)  # nosec


class User(AbstractUser):
    birthday = models.DateField()
    random_number = models.PositiveSmallIntegerField(default=generate_random_number)

    def get_absolute_url(self) -> str:
        return reverse('user-details', kwargs=dict(pk=self.pk))
