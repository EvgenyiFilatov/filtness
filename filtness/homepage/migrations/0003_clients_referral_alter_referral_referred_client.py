# Generated by Django 4.2.16 on 2024-09-26 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_referral'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='referral',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referral', to='homepage.referral', verbose_name='Реферал'),
        ),
        migrations.AlterField(
            model_name='referral',
            name='referred_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referred_client', to='homepage.clients', verbose_name='Реферал'),
        ),
    ]
