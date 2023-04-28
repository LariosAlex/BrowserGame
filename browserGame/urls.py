from django.urls import path
from . import views

urlpatterns = [
    path('vue', views.vue, name='index'),
    path('', views.landing, name='landing'),
]