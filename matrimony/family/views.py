from django.shortcuts import render
from rest_framework import viewsets
from .models import FamilyDetailes
from .serializer import FamilySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404 
# Create your views here.

'''class FamilyViewSet(viewsets.ModelViewSet):
    queryset = FamilyDetailes.objects.all()
    serializer_class = FamilySerializer'''

class FamilyView(APIView):
 
    def get(Self,request,pk=None):
        if pk:
            basic_info=FamilyDetailes.objects.get(pk=pk)
            serializer=FamilySerializer(basic_info)
            return Response(serializer.data)
       
        else:
            basic_info=FamilyDetailes.objects.all()
            serializer=FamilySerializer(basic_info,many=True)
            return Response(serializer.data)
 
 
    def post(self,request):
        serializer=FamilySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def put(self,request,pk):
        basic_info=FamilyDetailes.objects.get(pk=pk)
        serializer=FamilySerializer(basic_info,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def patch(self,request,pk):
        basic_info=FamilyDetailes.objects.get(pk=pk)
        serializer=FamilySerializer(basic_info,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def delete(self,request,pk):
        basic_info=FamilyDetailes.objects.get(pk=pk)
        basic_info.delete()
        return Response({"message":"Record Deleted....!!"})                              