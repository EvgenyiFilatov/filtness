from django.db import models
from django.contrib.auth import get_user_model

from treners.models import Treners
from user.models import MyUser


User = get_user_model()


class TrainingSessions(models.Model):
    """
    Модель, представляющая запись на тренировку.
    """
    trener = models.ForeignKey(
        Treners, on_delete=models.CASCADE, related_name='sessions')
    date_time = models.DateTimeField('Дата и время тренировки')
    author = models.ForeignKey(
        MyUser, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
    )

    class Meta:
        unique_together = ('trener', 'date_time')
