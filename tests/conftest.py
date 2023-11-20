import datetime

import pytest
from django.contrib.auth.models import User
from django.utils import timezone

from service.models import CDR


@pytest.fixture()
def user(db):
    return User.objects.create_user('test-user', 'example@example.com', 'password')


@pytest.fixture()
def cdr_1(db):
    started = timezone.now()
    ended = started + datetime.timedelta(minutes=1)

    return CDR.objects.create(
        calling_number='89086469500', called_number='89086469400',
        started=started, duration=datetime.time(1), status='SUCCESS',
        ended=ended + datetime.timedelta(minutes=1),
    )


@pytest.fixture()
def cdr_2(db):
    started = timezone.now()
    ended = started + datetime.timedelta(minutes=1)

    return CDR.objects.create(
        calling_number='89086469500', called_number='89086469400',
        started=started, duration=datetime.time(1), status='SUCCESS',
        ended=ended + datetime.timedelta(minutes=1),
    )


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()
