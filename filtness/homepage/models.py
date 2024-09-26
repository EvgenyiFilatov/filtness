from django.db import models


class Clients(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    birthday = models.DateField(
        'День рождения клиента',
        )
    created_at = models.DateTimeField(
        'Добавлено', auto_now_add=True)
    is_visiting = models.BooleanField(
        'Ходит или нет', default=True,
        help_text='Снимите галочку, если клиент не ходит.')

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Referral(models.Model):
    client = models.ForeignKey(
        Clients,
        on_delete=models.CASCADE,
        related_name='referrals',
        verbose_name='Клиент-реферал'
        )
    referred_client = models.ForeignKey(
        Clients,
        on_delete=models.CASCADE,
        related_name='referral_of',
        verbose_name='Реферал')

    class Meta:
        verbose_name = 'реферал'
        verbose_name_plural = 'Рефералы'

    def __str__(self):
        return f'{self.client} - {self.referred_client}'

