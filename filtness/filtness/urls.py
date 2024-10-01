from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('about/', include('about.urls')),
    path('sign_for_training/', include('sign_for_training.urls'))
]
