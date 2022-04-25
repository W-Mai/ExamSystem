import datetime
import json
from typing import Optional

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Manager, Model


def aware_to_native(aware_dt):
    """
    Convert aware datetime to naive datetime
    """
    return aware_dt.replace(tzinfo=None)


class BaseManager(Manager):
    def get(self, *args, **kwargs) -> Optional[Model]:
        try:
            return super().get(*args, **kwargs)
        except ObjectDoesNotExist:
            return None


class BaseModel(Model):
    class Meta:
        abstract = True

    objects = BaseManager()


def to_json(obj):
    """
    Convert object to json
    """
    return json.dumps(obj, separators=(",", ":"), ensure_ascii=False)
