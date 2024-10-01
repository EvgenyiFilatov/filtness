from django.db import models
from django.db import models
from homepage.models import Clients
from treners.models import Treners


class TrainingSessions(models.Model):
    """
    Модель, представляющая запись на тренировку.
    """
    trener = models.ForeignKey(
        Treners, on_delete=models.CASCADE, related_name='sessions')
    client = models.ForeignKey(
        Clients, on_delete=models.CASCADE, related_name='sessions')
    date_time = models.DateTimeField('Дата и время тренировки')

    class Meta:
        unique_together = ('trener', 'date_time')
