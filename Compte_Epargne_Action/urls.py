from Compte_Epargne_Action.views import PortfolioViewSet,PortfolioTitleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('portfolio', PortfolioViewSet, basename='portfolio')
router.register('portfolioTitle', PortfolioTitleViewSet, basename='portfolioTitle')
urlpatterns = router.urls
