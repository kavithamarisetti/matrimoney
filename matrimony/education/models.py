from django.db import models

# Create your models here.
from app.models import BasicInformation

class Education_Detailes(models.Model):
    basic_info = models.ForeignKey(BasicInformation, on_delete=models.CASCADE, related_name='education_details')
    qualification= models.CharField(max_length=15)
    occupations= models.CharField(max_length=15)
    occupation_Detailes=models.CharField(max_length=25)
    annual_income=models.IntegerField()
    employed_in=models.CharField(max_length=10)
    working_location=models.CharField(max_length=15)
    special_cases=models.CharField(max_length=15)