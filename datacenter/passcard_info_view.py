from datacenter.models import Passcard
from datacenter.models import Visit, format_duration
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits = []
    passcard_visits = Visit.objects.filter(passcard=passcard)
    for visit in passcard_visits:
        entered_time = visit.entered_at
        duration = visit.get_duration()
        formated_duration = format_duration(duration)
        is_strange = visit.is_visit_long()
        this_passcard_visits.append(
            {
                'entered_at': entered_time,
                'duration': formated_duration,
                'is_strange': is_strange
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
