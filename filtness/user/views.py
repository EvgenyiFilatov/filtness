from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from user.models import MyUser
from sign_for_training.models import TrainingSessions


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('homepage:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class ProfileView(DetailView):
    model = MyUser
    template_name = 'user/profile.html'
    context_object_name = 'profile'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.object
        sign_list = TrainingSessions.objects.filter(
            author=profile
            ).select_related(
            'author',
        ).order_by('-date_time',)
        
        context['sign_list'] = sign_list
        return context

