from django.db import models
from app.models import BasicInformation
# Create your models here.
CHOICES = [('My parents will stay with me after marriage', 'My parents will stay with me after marriage'),
                ('My parents will not stay with me after marriage', 'My parents will not stay with me after marriage'), 
                ('Dont wish to specify', 'Dont wish to specify')]
class FamilyDetailes(models.Model):
   
    basic_info = models.ForeignKey(BasicInformation, on_delete=models.CASCADE, related_name='family_details')
    family_values=models.CharField(max_length=100)
    family_type=models.CharField(max_length=100)
    family_status=models.CharField(max_length=100)
    no_ofbroders=models.IntegerField()
    no_ofbroders_married=models.IntegerField()
    no_ofsisters=models.IntegerField()
    no_ofsisters_married=models.IntegerField()
    mothertounge=models.CharField(max_length=70)
    fathername=models.CharField(max_length=100)
    fatheroccupation=models.CharField(max_length=150)
    mothername=models.CharField(max_length=100)
    motheroccupation=models.CharField(max_length=150)
    familywealth=models.TextField()
    aboutfamily=models.TextField()
    familystaychoice=models.CharField(max_length=60, choices=CHOICES)
    
    def __str__(self):
        return f" {self.family_values} - {self.family_status}"