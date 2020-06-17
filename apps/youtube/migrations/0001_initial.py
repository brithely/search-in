# Generated by Django 2.2.13 on 2020-06-17 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('published_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeChannelStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subscriber_count', models.IntegerField()),
                ('view_count', models.IntegerField()),
                ('comment_count', models.IntegerField()),
                ('video_count', models.IntegerField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='youtube.YoutubeChannel')),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeChannelSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='youtube.YoutubeChannel')),
            ],
        ),
    ]
