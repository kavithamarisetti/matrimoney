from django.db import models
from django.contrib.auth.models import User
# Create your models here. 
 
class PartnerPreferenceDetails(models.Model):
    LOOKING_FOR_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    COMPLEXION_CHOICES = [
        ('Fair', 'Fair'),
        ('Wheatish', 'Wheatish'),
        ('Dark', 'Dark'),
        ('Any', 'Any'),
    ]
    RESIDENCY_STATUS_CHOICES = [
        ('Citizen', 'Citizen'),
        ('Permanent Resident', 'Permanent Resident'),
        ('Temporary Resident', 'Temporary Resident'),
    ]
   
    looking_for = models.CharField(max_length=10, choices=LOOKING_FOR_CHOICES)
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    height_from = models.DecimalField(max_digits=4, decimal_places=2)
    height_to = models.DecimalField(max_digits=4, decimal_places=2)
    religion = models.CharField(max_length=50)
    caste = models.CharField(max_length=50)
    complexion = models.CharField(max_length=10, choices=COMPLEXION_CHOICES)
    residency_status = models.CharField(max_length=20, choices=RESIDENCY_STATUS_CHOICES)
    country = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    partner_expectations = models.TextField()
 
    def __str__(self):
        return f"Partner Preference for {self.looking_for}"
 
 
class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
 
    def __str__(self):
        return self.user.username
   
 
 
class SixPhoto(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='six_photos')
    pic1 = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    pic2 = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    pic3 = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    pic4 = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    pic5 = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    pic6 = models.ImageField(upload_to='user_photos/', null=True, blank=True)
 
    def __str__(self):
        return f"{self.user.username}'s Photos"
   
 
class IdProof(models.Model):
    id_proof = models.ImageField(upload_to='id_proofs/', null=True, blank=True)
    passport_size_photo = models.ImageField(upload_to='passport_photos/', null=True, blank=True)
 
    def __str__(self):
        return f"ID Proof {self.pk}"
   
 
 
class DocumentAddress(models.Model):
    address_id = models.ImageField(upload_to="address_id/",null=True,blank=True)  
    certificates = models.FileField(upload_to='certificates/', null=True, blank=True)
 
    def __str__(self):
        return f"Document Address {self.address_id}"
   
 
class CompatibilityMatch(models.Model):
    HOW_OFTEN_CHOICES = [
        ('Rarely', 'Rarely'),
        ('Occasionally', 'Occasionally'),
        ('Frequently', 'Frequently'),
        ('Always', 'Always'),
    ]
 
    SOCIAL_PLATFORM_CHOICES = [
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('Twitter', 'Twitter'),
        ('LinkedIn', 'LinkedIn'),
        ('Other', 'Other'),
    ]
 
    PERSONALITY_CHOICES = [
        ('Introvert', 'Introvert'),
        ('Extrovert', 'Extrovert'),
        ('Ambivert', 'Ambivert'),
    ]
 
    how_often_do_you_go_out = models.CharField(max_length=20, choices=HOW_OFTEN_CHOICES)
    how_would_you_describe_your_clothes = models.TextField()
    how_do_you_spend_your_free_time = models.TextField()
    how_many_times_do_you_visit_salon_or_beauty_parlour = models.PositiveIntegerField()
    how_many_times_do_you_go_out_drinking_or_in_a_pub = models.PositiveIntegerField()
    what_would_you_choose_for_a_romantic_date_with_your_partner = models.TextField()
    which_social_platform_do_you_use_most = models.CharField(max_length=20, choices=SOCIAL_PLATFORM_CHOICES)
    do_you_like_shopping = models.BooleanField()
    preferences_while_traveling = models.TextField()
    which_personality_are_you = models.CharField(max_length=20, choices=PERSONALITY_CHOICES)
 
    def __str__(self):
        return f"Compatibility Match {self.id}"
 
 
class ReviewSection(models.Model):
    user_profile = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.PositiveIntegerField()
    descriptions = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
 
    def __str__(self):
        return f"Review by {self.name} - Rating: {self.rating}"
 
 
 
class ProfileCompletes(models.Model):
    profile_photo = models.BooleanField()
    basic_details_completed = models.BooleanField()
    education_details_completed = models.BooleanField()
    horoscope_details_completed = models.BooleanField()
    family_details_completed = models.BooleanField()
    partner_preference_details_completed = models.BooleanField()
    habits_details_completed = models.BooleanField()
    hobbies_details_completed = models.BooleanField()
    interest_details_completed = models.BooleanField()
   
 
 
class Habits(models.Model):
    user_profile = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    habits = models.TextField(max_length=200)
 
 
 
class Hobbies(models.Model):
    user_profile = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    hobbies = models.TextField(max_length=200)    


STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
    ('Failed', 'Failed'),
]
 
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=100, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"Payment: {self.id} by {self.user.username}"

    
 
     