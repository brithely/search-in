from django.contrib import admin
from django.urls import path, include
from youtube.views import YoutubeChannelListView

urlpatterns = [
    path('list/', YoutubeChannelListView.as_view())
]
