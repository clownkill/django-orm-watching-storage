from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def format_duration(duration):
    from datetime import timedelta

    total_seconds = duration.total_seconds()
    time_format = str(timedelta(seconds=total_seconds))
    return time_format.split('.')[0]


def storage_information_view(request):
    # Программируем здесь
    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in visits:
        duration, en_time = visit.get_duration()
        formated_duration = format_duration(duration)
        who_entered = visit.passcard
        non_closed_visits.append(
            {
                'who_entered': who_entered,
                'entered_at': en_time,
                'duration': formated_duration,
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
