import datetime

from . import me
from .shop_models import TrackedDatesEntity


class News(TrackedDatesEntity):
    title = me.StringField(required=True, min_length=2, max_length=256)
    body = me.StringField(required=True, min_length=2, max_length=2048)

    @classmethod
    def get_latest(cls):
        return cls.objects().order_by('-modified')[:5]