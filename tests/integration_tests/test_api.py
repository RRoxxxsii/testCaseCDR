import datetime

import pytest
from django.urls import reverse
from django.utils import timezone
from rest_framework import status as http_status


def test_not_authorized(api_client, user, cdr_1):
    response = api_client.get(reverse('cdr-list'))
    assert response.status_code == http_status.HTTP_401_UNAUTHORIZED


def test_get_list_authorized(api_client, user, cdr_1, cdr_2):
    api_client.force_authenticate(user)
    response = api_client.get(reverse('cdr-list'))
    assert len(eval(response.content)) == 2
    assert response.status_code == http_status.HTTP_200_OK


def test_get_obj_by_id_authorized(api_client, user, cdr_1, cdr_2):
    api_client.force_authenticate(user)
    response = api_client.get(reverse('cdr-detail', args=[cdr_1.pk]))
    assert eval(response.content).get('id') == cdr_1.pk
    assert response.status_code == http_status.HTTP_200_OK


@pytest.mark.parametrize(
    'calling_number, called_number, started, duration, ended, status, validity_status',
    [
        ('88005553535', '88005553535', timezone.now(), datetime.time(1),
         timezone.now() + datetime.timedelta(minutes=1), 'success', http_status.HTTP_400_BAD_REQUEST),

        ('88005553535', '89086469500', timezone.now(), datetime.time(1),
         timezone.now() + datetime.timedelta(minutes=1), 'this_value_is_not_correct', http_status.HTTP_400_BAD_REQUEST),

        ('88005553535', '89086469500', timezone.now(), datetime.time(1),
         timezone.now() + datetime.timedelta(minutes=1), 'success', http_status.HTTP_201_CREATED)
    ]
)
def test_post(api_client, user, calling_number, called_number, started, duration, ended, status, validity_status):
    data = {
        'calling_number': calling_number,
        'called_number': called_number,
        'started': started,
        'duration': duration,
        'status': status,
        'ended': ended
    }
    api_client.force_authenticate(user)
    response = api_client.post(reverse('cdr-list'), data=data)
    assert response.status_code == validity_status


def test_delete(api_client, user, cdr_1, cdr_2):
    api_client.force_authenticate(user)
    response = api_client.delete(reverse('cdr-detail', args=[cdr_1.pk]))
    assert response.status_code == http_status.HTTP_204_NO_CONTENT
