from django.db import models
from django.conf import settings
from django.db.models.signals import post_save , pre_save
from django.core.mail import send_mail

# Create your models here.
class Register(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=6)
    confirm_password = models.CharField(max_length=6)
    phone_number = models.BigIntegerField(blank=True, null=True)
    otp = models.CharField(max_length=64, null=True, blank=True)  
    otp_expiry = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email

        
def inserthandler(sender,instance,*args,**kwargs):
        subject='Test email'
        message='''
        successfully registration completed 
        username - {}
        password  - {}  '''.format(instance.name,instance.password)


        # Correct the recipient_list to use the instance's email
        recipient_list = [instance.email]
        send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,  # Make sure EMAIL_HOST_USER is configured in your settings.py
        recipient_list=recipient_list
    )
        
    
post_save.connect(inserthandler,sender=Register)

