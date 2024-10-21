from django.shortcuts import render
from rest_framework import viewsets
from .models import ContactUs
from .serializer import ContactUsSerializer
from rest_framework.views import APIView 
from django.http import Http404 
from rest_framework import status
from rest_framework.response import Response
#from rest_framework_simplejwt.authentication import JWTAuthentication
#from rest_framework.permissions import IsAuthenticated

'''class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    #permission_classes=[IsAuthenticated]
    #authentication_classes=[JWTAuthentication]'''

class ContactView(APIView):
 
    def get(Self,request,pk=None):
        if pk:
            basic_info=ContactUs.objects.get(pk=pk)
            serializer=ContactUsSerializer(basic_info)
            return Response(serializer.data)
       
        else:
            basic_info=ContactUs.objects.all()
            serializer=ContactUsSerializer(basic_info,many=True)
            return Response(serializer.data)
 
 
    def post(self,request):
        serializer=ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def put(self,request,pk):
        basic_info=ContactUs.objects.get(pk=pk)
        serializer=ContactUsSerializer(basic_info,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def patch(self,request,pk):
        basic_info=ContactUs.objects.get(pk=pk)
        serializer=ContactUsSerializer(basic_info,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def delete(self,request,pk):
        basic_info=ContactUs.objects.get(pk=pk)
        basic_info.delete()
        return Response({"message":"Record Deleted....!!"})        