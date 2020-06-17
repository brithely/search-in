from django.db import models

# Create your models here.

class YoutubeChannel(models.Model):
    key = models.CharField(max_length=100)
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def snippet(self):
        if self.youtubechannelsnippet_set.all().exists():
            return self.youtubechannelsnippet_set.all().latest('created_at')
        else:
            return None

    @property
    def statistics(self):
        if self.youtubechannelstatistics_set.all().exists():
            return self.youtubechannelstatistics_set.all().latest('created_at')
        else:
            return None


class YoutubeChannelStatistics(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.ForeignKey(YoutubeChannel, on_delete=models.PROTECT)
    subscriber_count = models.IntegerField()
    view_count = models.IntegerField()
    comment_count = models.IntegerField()
    video_count = models.IntegerField()


class YoutubeChannelSnippet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.ForeignKey(YoutubeChannel, on_delete=models.PROTECT)
    title = models.CharField(max_length=500)
    description = models.TextField()
