from django.urls import path

from . import views


app_name = 'user'

urlpatterns = [
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('profile/<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('user/', views.edit_profile, name='edit_profile'),
]
