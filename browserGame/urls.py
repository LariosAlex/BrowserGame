from django.urls import path
from . import views, api
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.signup, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('reset_password/', views.password_reset, name='password_reset'),
    path('reset_password/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', views.landing, name='landing'),
    path('accio', views.accio, name='accio'),
    path('save_action/', views.save_action, name='save_action'),
    path('damage_character/', views.damage_character, name='damage_character'),
    path('update_character/', views.update_character, name='update_character'),

    path('activate_cron/', views.activate_cron, name='activate_cron'),
    path('ranking', views.ranking, name='landing'),

    path('api/getRanking/', api.getRanking, name='getRanking'),
    path('api/getCharacter/<int:character_id>', api.getCharacter, name='getCharacter'),
    path('api/getActionsLog/<int:character_id>', api.getActionsLog, name='getActionsLog'),
    path('api/getActions/', api.getActions, name='getActions'),
]