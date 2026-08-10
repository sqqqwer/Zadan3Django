from django.db.models import Avg, Count, IntegerField, OuterRef, Subquery
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny

from dogs.models import Breed, Dog
from dogs.serializers import (
    BreedListSerializer,
    BreedSerializer,
    DogListSerializer,
    DogRetrieveSerializer,
    DogSerializer,
)


class DogViewSet(viewsets.ModelViewSet):
    """Provide CRUD operations for the Dog model."""
    permission_classes = (AllowAny, )
    pagination_class = LimitOffsetPagination
    http_method_names = ('get', 'post', 'put', 'delete')

    def get_queryset(self):
        """Return a queryset for the current action.

        Returns:
            For the list action:
                A queryset of Dog objects annotated with the avg_breed_age field.
            For the retrieve action:
                A queryset of Dog objects annotated with the same_breed_count field.
            For all other actions:
                A standard queryset of Dog objects.
        """
        if self.action == 'list':
            avg_age_subquery = (
                Dog.objects
                .filter(breed=OuterRef("breed"))
                .values("breed")
                .annotate(avg_age=Avg("age"))
                .values("avg_age")
            )
            return Dog.objects.select_related("breed").annotate(
                avg_breed_age=Subquery(
                    avg_age_subquery, output_field=IntegerField()
                )
            )
        elif self.action == 'retrieve':
            return Dog.objects.select_related("breed").annotate(
                same_breed_count=Count("breed__dogs")
            )
        else:
            return Dog.objects.all()

    def get_serializer_class(self):
        """Return the serializer class for the current action.

        Returns:
            For the list action:
                DogListSerializer with the additional avg_breed_age field.
            For the retrieve action:
                DogRetrieveSerializer with the additional same_breed_count field.
            For all other actions:
                DogSerializer, the base serializer for the Dog model.
        """
        if self.action == 'list':
            return DogListSerializer
        elif self.action == 'retrieve':
            return DogRetrieveSerializer
        else:
            return DogSerializer

class BreedViewSet(viewsets.ModelViewSet):
    """Provide CRUD operations for the Breed model."""
    permission_classes = (AllowAny, )
    pagination_class = LimitOffsetPagination
    http_method_names = ('get', 'post', 'put', 'delete')

    def get_queryset(self):
        """Return a queryset for the current action.

        Returns:
            For the list action:
                A queryset of Breed objects annotated with the dogs_count field.
            For all other actions:
                A standard queryset of Breed objects.
        """
        if self.action == 'list':
            return Breed.objects.annotate(
                dogs_count=Count('dogs')
            )
        else:
            return Breed.objects.all()

    def get_serializer_class(self):
        """Return the serializer class for the current action.

        Returns:
            For the list action:
                BreedListSerializer with the additional dogs_count field.
            For all other actions:
                BreedSerializer, the base serializer for the Breed model.
        """
        if self.action == 'list':
            return BreedListSerializer
        else:
            return BreedSerializer

