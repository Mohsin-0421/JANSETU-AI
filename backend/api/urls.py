from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChallengeViewSet, UniversityViewSet, IndustryViewSet

router = DefaultRouter()
router.register(r'challenges', ChallengeViewSet)
router.register(r'universities', UniversityViewSet)
router.register(r'industries', IndustryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]