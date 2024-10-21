from rest_framework import serializers
from .models import PartnerPreferenceDetails,UserModel,SixPhoto,IdProof,DocumentAddress,CompatibilityMatch,ReviewSection,ProfileCompletes,Habits,Hobbies
from .models import Payment 
class PartnerPreferenceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerPreferenceDetails
        fields = '__all__'
 
 
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
 
 
class SixPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SixPhoto
        fields = "__all__"
 
class IdProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdProof
        fields = "__all__"
 
 
class DocumentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentAddress
        fields = "__all__"
 
 
 
class CompatibilityMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompatibilityMatch
        fields = "__all__"
 
 
 
class ReviewSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewSection
        fields = '__all__'
 
 
class ProfileCompletesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileCompletes
        fields = '__all__'
 
 
class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields='__all__'
 
class HobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbies
        fields='__all__'
 
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
         