from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CDR(models.Model):
    SUCCESS = 'success'
    MISSED = 'missed'
    DECLINED = 'declined'

    STATUS_CHOICES = [
        (SUCCESS, 'success'),
        (MISSED, 'missed'),
        (DECLINED, 'declined')
    ]

    calling_number = PhoneNumberField('Номер вызывающего абонента', region='RU')
    called_number = PhoneNumberField('Номер вызываемого абонента', region='RU')

    started = models.DateTimeField('Время начала вызова')
    ended = models.DateTimeField('Время окончания вызова')
    duration = models.TimeField('Продолжительность вызова')
    status = models.CharField('Статус', choices=STATUS_CHOICES)

    created = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Запись разговора'
        verbose_name_plural = 'Записи разговора'
