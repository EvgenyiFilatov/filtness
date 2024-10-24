from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView
from .forms import TrainingSessionForm
from .models import TrainingSessions


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


class SignEditView(LoginRequiredMixin, UpdateView):
    model = TrainingSessions
    form_class = TrainingSessionForm
    template_name = 'sign_for_training/edit_sign.html'

    def get_object(self):
        sign_id = self.kwargs.get('sign_id')
        return get_object_or_404(TrainingSessions, id=sign_id)

    def get_success_url(self):
        return reverse_lazy('user:profile', args=[self.request.user.username])


class SignDeleteView(LoginRequiredMixin, DeleteView):
    model = TrainingSessions
    template_name = 'sign_for_training/edit_sign.html'

    def get_object(self):
        sign_id = self.kwargs.get('sign_id')
        return get_object_or_404(TrainingSessions, id=sign_id)

    def get_success_url(self):
        return reverse_lazy('user:profile', args=[self.request.user.username])
