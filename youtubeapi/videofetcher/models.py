from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    publishing_datetime = models.DateTimeField()
    thumbnail_urls = models.JSONField()
    # Add any other fields you need

    class Meta:
        ordering = ['-publishing_datetime']
