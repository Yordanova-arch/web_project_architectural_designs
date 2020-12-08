from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


# Custom Validator
def is_negative(value):
    if value < 0:
        raise ValidationError('The value must be positive')


# Create your models here.
class Designs(models.Model):
    name = models.CharField(max_length=15, blank=False)
    total_area = models.IntegerField(blank=False,  validators=[is_negative, ])
    price = models.FloatField(blank=False,  validators=[is_negative, ])
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='designs', blank=False)

    image_floor_one = models.ImageField(upload_to='images_floors', blank=True)
    image_floor_two = models.ImageField(upload_to='images_floors', blank=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    stories = models.IntegerField(blank=False, validators=[is_negative, ])
    baths = models.IntegerField(blank=False, validators=[is_negative, ])
    beds = models.IntegerField(blank=False, validators=[is_negative, ])
    garages = models.IntegerField(blank=False,  validators=[is_negative, ])

    def __str__(self):
        return f'{self.id}; {self.name}; {self.price}'
