from django.urls import path

from . import views

app_name = 'sign_for_training'

urlpatterns = [
    path('', views.SignCreateView.as_view(), name='sign'),
    path(
        'sign/<int:sign_id>/edit/', views.SignEditView.as_view(), name='edit'
        ),
    path(
        'sign/<int:sign_id>/delete/',
        views.SignDeleteView.as_view(),
        name='delete'
        ),
]
