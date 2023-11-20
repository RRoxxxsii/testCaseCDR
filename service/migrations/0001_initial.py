# Generated by Django 4.2.7 on 2023-11-19 15:45

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CDR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calling_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер вызывающего абонента')),
                ('called_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер вызываемого абонента')),
                ('started', models.DateTimeField(verbose_name='Время начала вызова')),
                ('ended', models.DateTimeField(verbose_name='Время окончания вызова')),
                ('duration', models.TimeField(verbose_name='Продолжительность вызова')),
                ('status', models.CharField(choices=[('success', 'success'), ('missed', 'missed'), ('declined', 'declined')], verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Запись разговора',
                'verbose_name_plural': 'Записи разговора',
            },
        ),
    ]
