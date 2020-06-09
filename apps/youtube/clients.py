import requests
from django.conf import settings
from googleapiclient.discovery import build

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
            print(response.json())
            return response.json()
        else:
            return None 
