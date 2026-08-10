from django.urls import include, path
from rest_framework.routers import DefaultRouter

from dogs.views import BreedViewSet, DogViewSet

router = DefaultRouter()
router.register('dogs', DogViewSet, basename='dog')
router.register('breeds', BreedViewSet, basename='breed')

urlpatterns = [
    path('', include(router.urls))
]
