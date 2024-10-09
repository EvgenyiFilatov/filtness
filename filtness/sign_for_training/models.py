from django.db import models
from django.contrib.auth import get_user_model

from homepage.models import Clients
from treners.models import Treners


User = get_user_model()


class TrainingSessions(models.Model):
    """
    Модель, представляющая запись на тренировку.
    """
    trener = models.ForeignKey(
        Treners, on_delete=models.CASCADE, related_name='sessions')
    client = models.ForeignKey(
        Clients, on_delete=models.CASCADE, related_name='sessions')
    date_time = models.DateTimeField('Дата и время тренировки')
    author = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
    )

    class Meta:
        unique_together = ('trener', 'date_time')
