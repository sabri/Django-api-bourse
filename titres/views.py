from .models import Title
from .models import CompanyDetail
from .serializers import CompanyDetailserializers

from .serializers import Titleserializers
from rest_framework import viewsets
from account.permissions import IsLoggedInUserOrAdmin


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = Titleserializers
    queryset = Title.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list':
            permission_classes = [IsLoggedInUserOrAdmin]
        return [permission() for permission in permission_classes]


class CompanyDetailViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyDetailserializers
    queryset = CompanyDetail.objects.all()
