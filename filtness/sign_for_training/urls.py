from django.urls import path

from . import views

app_name = 'sign_for_training'

urlpatterns = [
    path('', views.SignCreateView.as_view(), name='sign'),
]
