from django.db import models
from django.contrib import admin


class Clients(models.Model):
    """
    Модель, представляющая клиента с его личной информацией
    и данными о рефералах.
    """
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    birthday = models.DateField(
        'День рождения клиента',
    )
    number_phone = models.CharField(
        'Номер телефона',
        blank=True,
        max_length=50
        )
    created_at = models.DateTimeField(
        'Добавлено', auto_now_add=True)
    is_visiting = models.BooleanField(
        'Ходит или нет', default=True,
        help_text='Снимите галочку, если клиент не ходит.')
    referral = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='referred_clients',
        verbose_name='Кто пригласил'
    )

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def discount_percentage(self):
        """Метод для расчета скидки в зависимости от количества рефералов."""
        referrals_count = self.referred_clients.count()
        if referrals_count == 0:
            return 0
        elif 1 <= referrals_count <= 5:
            return referrals_count * 5
        else:
            return 25  # Максимальная скидка

    @admin.display(description='Скидка (%)')
    def discount_percentage_display(self):
        """
        Возвращает название функции на русском языке в админ-панели.
        """
        return self.discount_percentage()
