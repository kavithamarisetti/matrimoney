from django.db import models
from app.models import BasicInformation
# Create your models here.

 
AM_PM_CHOICES = (
    ('AM', 'AM'),
    ('PM', 'PM'),
)
 
class HoroscopeDetails(models.Model):
    basic_info = models.ForeignKey(BasicInformation, on_delete=models.CASCADE, related_name='horoscope_details')
    moon_sign = models.CharField(max_length=50)
    star = models.CharField(max_length=50)
    gotra = models.CharField(max_length=50)
    manglik = models.BooleanField(default=False)
    shani = models.BooleanField(default=False)
    hororscope_match = models.BooleanField(default=False)
    place_of_birth = models.CharField(max_length=100)
    place_of_country = models.CharField(max_length=100)
    hours = models.IntegerField()
    minitues = models.IntegerField()
    seconds = models.IntegerField()
    am_pm = models.CharField(max_length=3, choices=AM_PM_CHOICES)
 
    def __str__(self):
        return f'{self.moon_sign} - {self.star}'