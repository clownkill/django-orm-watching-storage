from datacenter.models import Passcard
from datacenter.models import Visit, format_duration
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in visits:
        duration = visit.get_duration()
        formated_duration = format_duration(duration)
        who_entered = visit.passcard
        en_time = localtime(visit.entered_at)
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
