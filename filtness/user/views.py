from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from .forms import CustomUserCreationForm, UserProfileForm
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


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user:profile', username=user.username)
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'user/user.html', {'form': form})


@login_required
def change_password_view(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('blog:profile', username=user.username)
    else:
        form = PasswordChangeForm(user)
    return render(
        request, 'registration/password_change_form.html', {'form': form}
    )
