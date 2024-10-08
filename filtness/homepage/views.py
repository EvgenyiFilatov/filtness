from django.shortcuts import render
from django.utils import timezone
from .models import Clients
from user.models import MyUser


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

    users_with_birthday = MyUser.objects.filter(
            birthday__month=today.month,
            birthday__day=today.day
        )

    return render(
        request, 'homepage/birthday_today.html',
        {'users': users_with_birthday,
         'clients': clients_with_birthday,
         'clients_month': clients_with_birthday_in_month}
    )
