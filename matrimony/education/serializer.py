from rest_framework import serializers
from .models import Education_Detailes

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education_Detailes
        fields='__all__'