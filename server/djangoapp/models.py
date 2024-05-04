from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE
    )  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
        ("HATCHBACK", "Hatchback"),
        ("COUPE", "Coupe"),
        ("MINIVAN", "Minivan"),
        ("CONVERTIBLE", "Convertible"),
        ("PICKUP", "Pickup"),
    ]
    type = models.CharField(max_length=11, choices=CAR_TYPES, default="SUV")
    year = models.IntegerField(
        default=2023, validators=[MaxValueValidator(2023), MinValueValidator(2015)]
    )
    dealer_id = models.IntegerField()
    mileage = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
        ],
    )

    def __str__(self):
        return self.name  # Return the name as the string representation
