from django.core.management.base import BaseCommand
from django.utils import timezone
from videofetcher.models import Video
import requests
from datetime import datetime
import schedule
import time

from youtubeapi.videofetcher.utils import fetch_and_save_videos


class Command(BaseCommand):
    help = 'Schedule video fetching job'

    def handle(self, *args, **options):
        schedule.every(10).seconds.do(fetch_and_save_videos)  # Run every 10 seconds

        while True:
            schedule.run_pending()
            time.sleep(1)
