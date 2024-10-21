from rest_framework import serializers
from .models import FamilyDetailes

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyDetailes
        fields='__all__'