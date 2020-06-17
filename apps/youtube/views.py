import statistics

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from youtube.models import YoutubeChannel

class YoutubeChannelListView(APIView):
    
    def get(self, request, *args, **kwargs):
        channel_list = []
        for channel in YoutubeChannel.objects.all():
            snippet = channel.snippet
            statistics = channel.statistics
            channel = {
                'title': snippet.title,
                'description': snippet.description,
                'view_count': statistics.view_count,
                'subscriber_count': statistics.subscriber_count,
                'video_count': statistics.video_count,
            }
            channel_list.append(channel)
        return Response(
            status=status.HTTP_200_OK,
            data={"data": channel_list},
        )
