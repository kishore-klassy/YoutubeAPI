import requests
from datetime import datetime
from .models import Video

def fetch_and_save_videos():
    # Replace 'YOUR_API_KEY' with your actual YouTube Data API key
    api_key = 'AIzaSyAk_0ayo1aRDecJ0Ako3X00zYt-bfDO5D0'
    
    # Specify the search query and other parameters
    search_query = 'official'
    base_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'type': 'video',
        'order': 'date',
        'q': search_query,
        'maxResults': 100,  # Adjust the number of results as needed
        'key': api_key,
    }

    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check for errors in the response

        # Parse the JSON response
        data = response.json()

        # Extract video information and save to the database
        videos = data.get('items', [])
        for video in videos:
            snippet = video.get('snippet', {})
            title = snippet.get('title', '')
            description = snippet.get('description', '')
            published_at = snippet.get('publishedAt', '')
            thumbnail_urls = snippet.get('thumbnails', {}).get('default', {}).get('url', '')

            # Convert published_at to a datetime object
            published_datetime = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ')
            print("this is kishore checking))))))))))))))")
            # Save the video to the database
            Video.objects.create(
                title=title,
                description=description,
                publishing_datetime=published_datetime,
                thumbnail_urls=thumbnail_urls,
            )

    except requests.RequestException as e:
        print(f"Error making YouTube API request: {e}")

from django.core.management.base import BaseCommand
from django.utils import timezone
from videofetcher.models import Video
import requests
from datetime import datetime
import schedule
import time


class Command(BaseCommand):
    help = 'Schedule video fetching job'

    def handle(self, *args, **options):
        schedule.every(10).seconds.do(fetch_and_save_videos)  # Run every 10 seconds

        while True:
            schedule.run_pending()
            time.sleep(1)
