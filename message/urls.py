# root for application

from django.contrib import admin

from django.urls import path, include

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from message.views import send_message, LoginView
from message.viewsets import Chat_roomViewSet, MessageViewSet

router = DefaultRouter()

router.register(r"chat_rooms", Chat_roomViewSet, basename='chat_room')
router.register(r"messages", MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
    path('send_message/', send_message, name='send_message'),
    path('login/',LoginView.as_view(), name='login'),
]