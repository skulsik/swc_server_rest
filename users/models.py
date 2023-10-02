from django.contrib.auth.models import AbstractUser
from django.db import models

from services.utils import NULLABLE


class User(AbstractUser):
    date_of_birth = models.DateField(verbose_name='Дата рождения', **NULLABLE)
