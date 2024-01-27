from django.core.management.base import BaseCommand
from django.utils import timezone
from videofetcher.models import Video

class Command(BaseCommand):
    help = 'Populate Video model with sample data'

    def handle(self, *args, **options):
        # Clear existing data (optional)
        Video.objects.all().delete()

        # Populate with sample data
        for i in range(20):  # Adjust the number of videos as needed
            Video.objects.create(
                title=f"Sample Video {i+1}",
                description=f"This is a sample video #{i+1}",
                publishing_datetime=timezone.now(),
                thumbnail_urls={'default': 'sample_thumbnail_url'},
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated videos'))
