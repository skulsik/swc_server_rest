from django.db import models
from config import settings
from services.utils import NULLABLE
from users.models import User


class Event(models.Model):
    """ Модель событие """
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.CharField(max_length=1500, verbose_name='Текст события')
    date_of_creation = models.DateField(auto_now_add=True, verbose_name='Дата и время создания')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name='Владелец',
        **NULLABLE
    )
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="user_event",
        verbose_name='Пользователи'
    )

    def __str__(self):
        return f'Объект Event: {self.title}'

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
