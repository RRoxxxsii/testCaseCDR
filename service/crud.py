from abc import ABC, abstractmethod
from datetime import datetime
from time import time

from django.db.models import QuerySet

from service.models import CDR


class EntityAbstract(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(
            self, calling_number: str, called_number: str,
            started: datetime, ended: datetime, duration: time
    ):
        pass


class CDRCrud(EntityAbstract):
    model = CDR

    @classmethod
    def get_all(cls) -> QuerySet[CDR]:
        return cls.model.objects.all()

    @classmethod
    def create(
            cls, calling_number: str, called_number: str,
            started: datetime, ended: datetime, duration: time
    ) -> CDR:

        return cls.model.objects.create(
            calling_number=calling_number, called_number=called_number,
            started=started, ended=ended, duration=duration
        )
