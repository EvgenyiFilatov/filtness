# Generated by Django 4.2.16 on 2024-09-26 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_clients_referral_alter_referral_referred_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='referral',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referred_clients', to='homepage.clients', verbose_name='Реферал'),
        ),
        migrations.DeleteModel(
            name='Referral',
        ),
    ]