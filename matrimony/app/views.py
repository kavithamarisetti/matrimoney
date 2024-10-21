from django.shortcuts import render
from rest_framework.views import APIView 
from django.http import Http404 
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .models import BasicInformation
from .serializer import BasicInformationSerializer

'''class BasicInformationViewSet(viewsets.ModelViewSet):
    queryset = BasicInformation.objects.all()
    serializer_class = BasicInformationSerializer''' 
 
#Basic Information Views
class BasicInforView(APIView):
 
    def get(Self,request,pk=None):
        if pk:
            basic_info=BasicInformation.objects.get(pk=pk)
            serializer=BasicInformationSerializer(basic_info)
            return Response(serializer.data)
       
        else:
            basic_info=BasicInformation.objects.all()
            serializer=BasicInformationSerializer(basic_info,many=True)
            return Response(serializer.data)
 
 
    def post(self,request):
        serializer=BasicInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def put(self,request,pk):
        basic_info=BasicInformation.objects.get(pk=pk)
        serializer=BasicInformationSerializer(basic_info,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def patch(self,request,pk):
        basic_info=BasicInformation.objects.get(pk=pk)
        serializer=BasicInformationSerializer(basic_info,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def delete(self,request,pk):
        basic_info=BasicInformation.objects.get(pk=pk)
        basic_info.delete()
        return Response({"message":"Record Deleted....!!"})    