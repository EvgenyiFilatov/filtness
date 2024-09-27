from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from homepage.models import Clients


class Specialty(models.Model):
    """
    Модель, представляющая специализацию тренера.
    """
    name = models.CharField('Название специализации', max_length=100)

    class Meta:
        verbose_name = 'специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.name


class Treners(models.Model):
    """
    Модель, представляющая всю информацию о тренерах.
    """
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    specialties = models.ManyToManyField(
        Specialty,
        verbose_name='Специализации',
        related_name='trainers'
    )
    birthday = models.DateField(
        'День рождения тренера',
    )
    number_phone = models.CharField(
        'Номер телефона', blank=True, max_length=50)

    class Meta:
        verbose_name = 'тренер'
        verbose_name_plural = 'Тренеры'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ClientTrainerRelationship(models.Model):
    """
    Модель для связи между клиентами и тренерами.
    """
    client = models.ForeignKey(
        Clients,
        on_delete=models.CASCADE,
        related_name='trainer_relationships',
        verbose_name='Клиент'
    )
    trainer = models.ForeignKey(
        Treners,
        on_delete=models.CASCADE,
        related_name='client_relationships',
        verbose_name='Тренер'
    )
    fee = models.IntegerField('Комиссия тренера', default=45)
    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.CASCADE,
        verbose_name='Направление тренировок'
    )
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания', null=True, blank=True)

    class Meta:
        verbose_name = 'связь между клиентом и тренером'
        verbose_name_plural = 'Связи между клиентами и тренерами'

    def __str__(self):
        return f'{self.client} - {self.trainer}'

    def clean(self):
        # Проверка, что специальность доступна у тренера
        if self.specialty not in self.trainer.specialties.all():
            raise ValidationError(
                _('Специальность не доступна у данного тренера.'))
