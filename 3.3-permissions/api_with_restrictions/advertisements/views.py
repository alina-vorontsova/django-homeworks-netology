from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend

from .models import Advertisement
from .serializers import AdvertisementSerializer 
from .filters import AdvertisementFilter
from .permissions import IsOwnerOrAdmin


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer 
    filterset_class = AdvertisementFilter 
    filter_backends = [DjangoFilterBackend]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdmin()]
        else: 
            return [AllowAny()]