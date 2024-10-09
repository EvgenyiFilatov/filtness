from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import TrainingSessionForm


@login_required
def sign(request):
    training_session = None

    if request.method == 'POST':
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            training_session = form.save()
            training_session.save()
            messages.success(request, 'Запись на тренировку успешно создана!')
    else:
        form = TrainingSessionForm()

    return render(request, 'sign_for_training/sign.html',
                  {'form': form, 'training_session': training_session})

