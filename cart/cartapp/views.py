from django.shortcuts import render

from .models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import login
# Create your views here.


class createuser(APIView):
    def post(self,request,format=None):
        print(request.data,';;;;;;;;')
        serializer = userserializer(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            usercartser = Usercart()
            profile = userProfile()
            obj = user.objects.get(Phone_Number = serializer.data['Phone_Number'])
            print(obj,'objjjjj')
            usercartser.owner = obj
            profile.owner = obj
            profile.Name = request.data['Name']
            profile.Date_of_birth = request.data['Date_of_birth']
            profile.Gender = request.data['Gender']
            profile.Image = request.data['Image']
            profile.save()
            usercartser.save()
            print(usercartser,'usercartser usercartser usercartser')
            return Response(serializer.data)
        else:
            return Response({'msg':'Some thing went worng...','error':serializer.errors})
    def get(self,request,format=None):
        obj = user.objects.all()
        ser = userserializer(obj,many=True)
        
        return Response(ser.data)

class createproduct(APIView):
     def post(self,request,format=None):
        print(request.data,';;;;;;;;')
        serializer = productserializer(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'msg':'Some thing went worng...','error':serializer.errors})
        

class createproductimg(APIView):
    def post(self,request,format=None):
        print(request.data,';;;;;;;;')
        serializer = productimgserializer(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'msg':'Some thing went worng...','error':serializer.errors})

    def get(self,request,format=None):
        obj = productImage.objects.all()
        ser = productimgserializer(obj,many=True)
        
        return Response(ser.data)

class sendotp(APIView):
    def post(self,request,format=None):
        print(request.data,';;;;;;;;')
        serializer = userloginotpserializer(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'msg':'Some thing went worng...','error':serializer.errors})

class loginwithotp(APIView):
    def post(self,request,format=None):
    
        email = request.data['email']
        otp = request.data['otp']
        try:
            user = userloginOTP.objects.get(owner__Email_ID = email,otp=otp,active=1)
        except:
            user = None
        if user is not None:
            return Response({'msg':'User authenticated'})
        else:
            return Response({'msg':"User authentication failed.."})

class addcart(APIView):
     def post(self,request,format=None):
        print(request.data,';;;;;;;;')
        serializer = userloginotpserializer(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'msg':'Some thing went worng...','error':serializer.errors})