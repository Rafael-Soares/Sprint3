from os import name
from typing import NamedTuple
from django.contrib import admin
from django.urls import path
from . import views
#importação para redefinição de senha
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    #paths de redefinição de senha
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password" ),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete" ),

]
