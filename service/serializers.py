from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from service.models import CDR


class CDRSerializer(serializers.ModelSerializer):

    calling_number = PhoneNumberField(required=True, region='RU')
    called_number = PhoneNumberField(required=True, region='RU')

    class Meta:
        fields = '__all__'
        model = CDR

    def validate(self, attrs):
        if attrs['calling_number'] == attrs['called_number']:
            raise serializers.ValidationError('Номера телефона не должны совпадать.')
        if attrs['started'] > attrs['ended']:
            raise serializers.ValidationError('Время начала не может быть больше времени конца.')
        return attrs


class CDRListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CDR
        fields = ('id', 'created', 'calling_number', 'called_number', 'status')
