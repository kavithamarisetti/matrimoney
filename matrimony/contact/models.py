from django.db import models

# Create your models here.
from django.db import models
from app.models import BasicInformation

class ContactUs(models.Model):
    basic_info = models.ForeignKey(BasicInformation, on_delete=models.CASCADE, related_name='contact_details')
    mobile_number = models.CharField(max_length=15)
    alternative_mobile_number = models.CharField(max_length=15, blank=True)
    convenient_time_to_call = models.CharField(max_length=100)
    email = models.EmailField()
    show_permanent_address = models.TextField()
    show_working_address = models.TextField()
    
    

    def _str_(self):
        return self.email 