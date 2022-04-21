from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from fast_sample_django import views


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('health/', views.health),
    path('run_task/', views.run_task),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
