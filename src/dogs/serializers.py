from rest_framework import serializers

from dogs.models import Breed, Dog


class DogSerializer(serializers.ModelSerializer):
    """Serializer for Dog model."""

    breed = serializers.PrimaryKeyRelatedField(
        queryset=Breed.objects.all()
    )

    class Meta:
        fields = ('id', 'name', 'age', 'breed',
                  'gender', 'color', 'favorite_food', 'favorite_toy')
        model = Dog

class DogListSerializer(DogSerializer):
    """Serializer for Dog model on list action."""

    avg_breed_age = serializers.IntegerField(read_only=True)

    class Meta(DogSerializer.Meta):
        fields = (*DogSerializer.Meta.fields, 'avg_breed_age')

class DogRetrieveSerializer(DogSerializer):
    """Serializer for Dog model on retrieve action."""

    same_breed_count = serializers.IntegerField(read_only=True)

    class Meta(DogSerializer.Meta):
        fields = (*DogSerializer.Meta.fields, 'same_breed_count')

class BreedSerializer(serializers.ModelSerializer):
    """Serializer for Breed model."""

    class Meta:
        fields = ('id', 'name', 'size', 'friendliness',
                  'trainability', 'shedding_amount', 'exercise_needs')
        model = Breed

class BreedListSerializer(BreedSerializer):
    """Serializer for Breed model on list action."""

    dogs_count = serializers.IntegerField(read_only=True)

    class Meta(BreedSerializer.Meta):
        fields = (*BreedSerializer.Meta.fields, 'dogs_count')

