import datetime

import pytest
from django.utils import timezone

from service.serializers import CDRSerializer


@pytest.mark.parametrize(
    'calling_number, called_number, started, duration, ended, status, validity',
    [
        ('88005553535', '88005553535', timezone.now(), datetime.time(1),
         timezone.now() + datetime.timedelta(minutes=1), 'success', False),

        ('88005553535', '89086469500', timezone.now(), datetime.time(1),
         timezone.now() + datetime.timedelta(minutes=1), 'this_value_is_not_correct', False),

        ('88005553535', '89086469500', timezone.now(), datetime.time(1),
         timezone.now() + datetime.timedelta(minutes=1), 'success', True)
    ]
)
def test_serializer_input(calling_number, called_number, started, duration, ended, status, validity):
    data = {
        'calling_number': calling_number,
        'called_number': called_number,
        'started': started,
        'duration': duration,
        'status': status,
        'ended': ended
    }
    serializer = CDRSerializer(data=data)
    result = serializer.is_valid()
    assert result is validity
