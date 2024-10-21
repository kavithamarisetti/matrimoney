from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import HoroscopeDetails
from .serializer import HoroscopeDetailsSerializer
 
class HoroscopeDetailsView(APIView):
   
    def get(self, request, pk=None):
        if pk:
            horoscope_detail = get_object_or_404(HoroscopeDetails, pk=pk)
            serializer = HoroscopeDetailsSerializer(horoscope_detail)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            horoscope_details = HoroscopeDetails.objects.all()
            serializer = HoroscopeDetailsSerializer(horoscope_details, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
 
    def post(self, request):
        serializer = HoroscopeDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self, request, pk):
        horoscope_detail = get_object_or_404(HoroscopeDetails, pk=pk)
        serializer = HoroscopeDetailsSerializer(horoscope_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def patch(self, request, pk):
        horoscope_detail = get_object_or_404(HoroscopeDetails, pk=pk)
        serializer = HoroscopeDetailsSerializer(horoscope_detail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk):
        horoscope_detail = get_object_or_404(HoroscopeDetails, pk=pk)
        horoscope_detail.delete()
        return Response({"message": "Record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
 