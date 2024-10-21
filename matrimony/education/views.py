from django.shortcuts import render
from rest_framework import viewsets
from .models import Education_Detailes
from .serializer import EducationSerializer
from rest_framework.views import APIView 
from django.http import Http404 
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

'''class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education_Detailes.objects.all()
    serializer_class = EducationSerializer'''
class EducationView(APIView):
 
    def get(Self,request,pk=None):
        if pk:
            basic_info=Education_Detailes.objects.get(pk=pk)
            serializer=EducationSerializer(basic_info)
            return Response(serializer.data)
       
        else:
            basic_info=Education_Detailes.objects.all()
            serializer=EducationSerializer(basic_info,many=True)
            return Response(serializer.data)
 
 
    def post(self,request):
        serializer=EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def put(self,request,pk):
        basic_info=Education_Detailes.objects.get(pk=pk)
        serializer=EducationSerializer(basic_info,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def patch(self,request,pk):
        basic_info=Education_Detailes.objects.get(pk=pk)
        serializer=EducationSerializer(basic_info,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def delete(self,request,pk):
        basic_info=Education_Detailes.objects.get(pk=pk)
        basic_info.delete()
        return Response({"message":"Record Deleted....!!"})            