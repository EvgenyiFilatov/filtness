from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, DeleteView, UpdateView, ListView, DetailView
)
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


class SignCreateView(LoginRequiredMixin, CreateView):
    form_class = TrainingSessionForm
    template_name = 'sign_for_training/sign.html'

    def form_valid(self, form):
        sign = form.save(commit=False)
        sign.author = self.request.user
        sign.save()
        return redirect(
            reverse('user:profile', args=[self.request.user.username])
        )