from django.shortcuts import render
from django.utils import timezone
from .models import Clients


def index(request):
    template = 'homepage/index.html'
    return render(request, template)


def birthday_today(request):
    today = timezone.now().date()

    clients_with_birthday = Clients.objects.filter(
        birthday__month=today.month,
        birthday__day=today.day
    )
    clients_with_birthday_in_month = Clients.objects.filter(
        birthday__month=today.month,
    )

    return render(
        request, 'homepage/birthday_today.html',
        {'clients': clients_with_birthday,
         'clients_month': clients_with_birthday_in_month}
    )
