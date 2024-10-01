from django import forms
from .models import Clients, Treners, TrainingSessions
from django.utils import timezone


class TrainingSessionForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        queryset=Clients.objects.all(),
        label='Клиент',
        empty_label="Выберите клиента",  # Можно добавить текст по умолчанию
        required=True  # Сделаем выбор клиента обязательным
    )
    trener = forms.ModelChoiceField(
        queryset=Treners.objects.all(),
        label='Тренер',
        required=True
    )
    date_time = forms.DateTimeField(
        label='Дата и время тренировки',
        required=True,
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control',  # Дополнительный класс для стилизации
        }),
        initial=timezone.now().date
    )

    class Meta:
        model = TrainingSessions
        fields = ['client', 'trener', 'date_time']

    # def clean(self):
    #     cleaned_data = super().clean()
    #     date_time = cleaned_data.get('date_time')
    #     trener = cleaned_data.get('trener')

    #     # if TrainingSessions.objects.filter(trener=trener, date_time=date_time).exists():
    #         # raise forms.ValidationError('Выбранное время уже занято для этого тренера.')

    #     # return cleaned_data
