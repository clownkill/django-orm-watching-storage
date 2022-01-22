from datetime import timedelta
from django.db import models
from django.utils.timezone import localtime, now


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )

    def get_duration(self):
        entered_time = localtime(self.entered_at)
        leaved_time = localtime(self.leaved_at)
        delta = leaved_time - entered_time
        return delta

    def is_visit_long(self, minutes=60):
        visit_time = self.get_duration()
        return visit_time.total_seconds() // 60 > minutes


def format_duration(duration):
    total_seconds = duration.total_seconds()
    time_format = str(timedelta(seconds=total_seconds))
    return time_format.split('.')[0]
