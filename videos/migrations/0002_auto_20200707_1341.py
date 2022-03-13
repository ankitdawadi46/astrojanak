# Generated by Django 3.0.4 on 2020-07-07 07:56

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='video_link',
        ),
        migrations.AddField(
            model_name='videos',
            name='video',
            field=embed_video.fields.EmbedVideoField(default='https://www.youtube.com/watch?v=USBNA9XvAjw'),
        ),
    ]