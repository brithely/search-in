import requests
from django.conf import settings
from youtube.models import YoutubeChannel, YoutubeChannelSnippet, YoutubeChannelStatistics
from googleapiclient.discovery import build
import datetime

from searchin.settings import GOOGLE_API_KEY


class YoutubeAPI(object):

    def __init__(self):
        super().__init__()
        self.api_key = settings.GOOGLE_API_KEY
        self.youtube_service = build('youtube', 'v3', developerKey=self.api_key)

    def get_channels(self, channel_id=None):
        if channel_id:
            part = "id, snippet, brandingSettings, contentDetails, invideoPromotion, statistics, topicDetails"
            request_url = self.youtube_service.channels().list(part=part, id=channel_id).uri
            response = requests.get(url=request_url)
            json_data = response.json()
            items = json_data.get('items')
            item = items[0]
            snippet = item.get('snippet')
            statistics = item.get('statistics')
            published_at = datetime.datetime.strptime(snippet.get('publishedAt'), '%Y-%m-%dT%H:%M:%SZ')
            if snippet:
                channel = YoutubeChannel.objects.get_or_create(key=channel_id, published_at=published_at)[0]
                YoutubeChannelSnippet.objects.get_or_create(channel=channel, title=snippet.get('title'), description=snippet.get('description'))
                YoutubeChannelStatistics.objects.get_or_create(
                    channel=channel,
                    view_count=statistics.get('viewCount', 0), 
                    comment_count=statistics.get('commentCount', 0),
                    subscriber_count=statistics.get('subscriberCount', 0),
                    video_count=statistics.get('videoCount', 0))
            return response.json()
        else:
            return None 
