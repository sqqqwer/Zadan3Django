from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from dogs.constants import (
    BREED_MAX_INTEGER,
    BREED_MIN_INTEGER,
    BREED_NAME_CHAR_MAX_LENGTH,
    DOG_COLOR_CHAR_MAX_LENGTH,
    DOG_FAVORITE_FOOD_CHAR_MAX_LENGTH,
    DOG_FAVORITE_TOY_CHAR_MAX_LENGTH,
    DOG_GENDER_CHAR_MAX_LENGTH,
    DOG_NAME_CHAR_MAX_LENGTH,
)


class Breed(models.Model):
    """Represent a dog breed.

    Attributes:
        name: The breed name.
        size: The breed size category.
        friendliness: The breed friendliness rating.
        trainability: The breed trainability rating.
        shedding_amount: The breed shedding rating.
        exercise_needs: The breed exercise needs rating.
    """

    class Size(models.TextChoices):
        """Define the available choices for the breed size field."""

        TINY = 'tiny', 'Миниатюрная'
        SMALL = 'small', 'Маленькая'
        MEDIUM = 'medium', 'Средняя'
        LARGE = 'large', 'Крупная'

    max_size_length = max(len(value) for value in Size.values)
    integer_min_max_validators = (
        MinValueValidator(BREED_MIN_INTEGER),
        MaxValueValidator(BREED_MAX_INTEGER),
    )

    name = models.CharField(
        'Название',
        max_length=BREED_NAME_CHAR_MAX_LENGTH,
        unique=True
    )
    size = models.CharField(
        'Размер',
        max_length=max_size_length,
        choices=Size.choices
    )
    friendliness = models.IntegerField(
        'Дружелюбие',
        validators=integer_min_max_validators
    )
    trainability = models.IntegerField(
        'Обучаемость',
        validators=integer_min_max_validators
    )
    shedding_amount = models.IntegerField(
        'Интенсивность линьки',
        validators=integer_min_max_validators
    )
    exercise_needs = models.IntegerField(
        'Потребность в активности',
        validators=integer_min_max_validators
    )

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'Породы'

    def __str__(self) -> str:
        return self.name


class Dog(models.Model):
    """Represent a dog.

    Attributes:
        name: The dog name.
        age: The dog age.
        breed: The breed to which the dog belongs.
        gender: The dog gender.
        color: The dog color.
        favorite_food: The dog favorite food.
        favorite_toy: The dog favorite toy.
    """

    name = models.CharField(
        'Имя',
        max_length=DOG_NAME_CHAR_MAX_LENGTH
    )
    age = models.IntegerField(
        'Возраст',
        validators=(MinValueValidator(0),)
    )
    breed = models.ForeignKey(
        Breed,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Порода'
    )
    gender = models.CharField(
        'Пол',
        max_length=DOG_GENDER_CHAR_MAX_LENGTH
    )
    color = models.CharField(
        'Цвет',
        max_length=DOG_COLOR_CHAR_MAX_LENGTH
    )
    favorite_food = models.CharField(
        'Любимая еда',
        max_length=DOG_FAVORITE_FOOD_CHAR_MAX_LENGTH
    )
    favorite_toy = models.CharField(
        'Любимая игрушка',
        max_length=DOG_FAVORITE_TOY_CHAR_MAX_LENGTH
    )

    class Meta:
        default_related_name = 'dogs'
        verbose_name = 'собака'
        verbose_name_plural = 'Собаки'

    def __str__(self) -> str:
        return self.name
