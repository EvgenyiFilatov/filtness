# Generated by Django 4.2.16 on 2024-09-27 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treners', '0002_clienttrainerrelationship_specialty'),
    ]

    operations = [
        migrations.AddField(
            model_name='clienttrainerrelationship',
            name='fee',
            field=models.IntegerField(default=45, verbose_name='Комиссия тренера'),
        ),
    ]
