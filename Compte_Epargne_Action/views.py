from rest_framework import viewsets

from Compte_Epargne_Action.models import Portfolio, PortfolioTitle
from Compte_Epargne_Action.serializers import PortfolioSerializer, PortfolioTitleSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class PortfolioTitleViewSet(viewsets.ModelViewSet):
    queryset = PortfolioTitle.objects.all()
    serializer_class = PortfolioTitleSerializer

