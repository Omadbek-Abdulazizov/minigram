from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import home,register,profile,send_chat,get_messages

urlpatterns = [
    path('', home, name='chat-home'),
    path('login/', auth_views.LoginView.as_view(template_name="chat/login.html"), name='chat-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="chat/logout.html"), name='chat-logout'),
    path('register/', register, name='chat-register'),
    path('home/', home, name='chat-home'),
    path('profile/', profile, name='chat-profile'),
    path('send/', send_chat, name='chat-send'),
    path('renew/', get_messages, name='chat-renew'),
]
