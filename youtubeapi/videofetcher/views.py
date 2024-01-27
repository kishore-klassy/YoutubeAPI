from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer

class VideoListView(APIView):
    pagination_class = PageNumberPagination

    def get(self, request, format=None):
        # Your logic to fetch videos
        videos = Video.objects.all()
        
        # Paginate the queryset
        paginated_videos = self.pagination_class().paginate_queryset(videos, request, view=self)

        # Serialize the paginated data
        serializer = VideoSerializer(paginated_videos, many=True)

        return Response(serializer.data)
