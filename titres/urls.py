from titres.views import TitleViewSet
from rest_framework.routers import DefaultRouter
from titres.views import CompanyDetailViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('title', TitleViewSet, basename='titles')
router.register('company', CompanyDetailViewSet, basename='company detail')
urlpatterns = router.urls
