from django.urls import path
from . import views
from .views import activate_cron

urlpatterns = [
    path('', views.index, name='index'),
    path('activate_cron/', activate_cron, name='activate_cron'),
]