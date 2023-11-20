import datetime

import pytest
from django.utils import timezone

from service.crud import CDRCrud


def test_get_all(cdr_1, cdr_2):
    result = CDRCrud.get_all()
    assert len(result) == 2


@pytest.mark.django_db
def test_create():
    started = timezone.now()
    ended = started + datetime.timedelta(minutes=1)

    cdr = CDRCrud.create(
        calling_number='89086469500', called_number='89086469400',
        started=started, duration=datetime.time(1),
        ended=ended + datetime.timedelta(minutes=1),
    )

    assert cdr is not None
