from django.urls import path

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.index, name='index'),
    path('birthday_today/', views.birthday_today, name='birthday_today')
]
