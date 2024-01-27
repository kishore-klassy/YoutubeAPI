from django.urls import path
from .views import VideoListView

urlpatterns = [
    path('videos/', VideoListView.as_view(), name='video-list'),
    # Add any other URLs you may need
]
