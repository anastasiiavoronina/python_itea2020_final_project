import mongoengine as me
import datetime

me.connect('SHOP')


class TrackedDatesEntity(me.Document):
    created = me.DateTimeField()
    modified = me.DateTimeField()

    def save(self, *args, **kwargs):
        if self.id is None:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        super().save(*args, **kwargs)


class User(me.Document):
    telegram_id = me.IntField(primary_key=True)
    username = me.StringField(min_length=2, max_length=128)
    phone_number = me.StringField(max_length=12)
    email = me.EmailField()
    is_blocked = me.BooleanField(default=False)