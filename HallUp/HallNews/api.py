from HallNews.models import HallNew
from rest_framework import viewsets, permissions
from .serializer import HallNewsSerializer

#Lead Viewset
class HallNewsViewset(viewsets.ModelViewSet):
    queryset = HallNew.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HallNewsSerializer