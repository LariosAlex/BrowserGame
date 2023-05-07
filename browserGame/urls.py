from django.urls import path
from . import views, api
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.signup, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('reset_password/', views.password_reset, name='password_reset'),
    path('reset_password/done/', views.password_reset_done),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', views.landing, name='landing'),
    #path('activate_cron/', views.activate_cron, name='activate_cron'),
    path('ranking', views.ranking, name='landing'),

    path('api/getRanking/', api.getRanking, name='getRanking'),
]