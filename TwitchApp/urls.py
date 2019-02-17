from django.urls import path
from TwitchApp.main.views import login_page, twitch_auth, watch_stream

urlpatterns = [
    path('', login_page),
    path('twitch_auth', twitch_auth),
    path('watch_stream', watch_stream)
]
