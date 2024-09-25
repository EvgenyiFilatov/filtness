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
        return self.last_name
