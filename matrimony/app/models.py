from django.db import models

# Create your models here.
class BasicInformation(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    MARITAL_STATUS_CHOICES = [('S', 'Single'), ('M', 'Married'), ('D', 'Divorced')]
    
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    dob = models.DateField()
    age = models.IntegerField()
    height = models.DecimalField(max_digits=4, decimal_places=2)  # Example: 5.10 for height
    blood_group = models.CharField(max_length=3)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    religion = models.CharField(max_length=100)
    profile_created_by = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
    your_religion = models.CharField(max_length=100)
    your_caste = models.CharField(max_length=100)
    sub_caste = models.CharField(max_length=100, blank=True)
    about_yourself = models.TextField()

    def _str_(self):
        return f"{self.name} {self.surname}"