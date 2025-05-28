from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .forms import *
from rest_framework import viewsets
from django.contrib.auth import authenticate,login,logout
from .serializers import *
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
user = get_user_model()
# Create your views here.
def home(request):
               location_data = ambulanceCurrentLocation.objects.first()
               context={'location_data':location_data}
               return render(request,'index.html',context)

def addAmbulance(request):
       if request.method =='POST':
          form = Ambulancef(request.POST,request.FILES)
          if form.is_valid():
              form.save()
              messages.success(request,'Data has been uploaded!')
              return redirect('index')
       else:
          form = Ambulancef()

       return render(request,"templates/ambulance_forms.html",{'form':form})

def editAmbulance(request,pk):
       dataget = ambulance.objects.get(pk=pk)
       form = Ambulancef(instance=dataget)
       if request.method =='POST':
          form = Ambulancef(request.POST,request.FILES,instance=dataget)
          if form.is_valid():
            form.save()
            messages.success(request,'Data has been Edited!')
            return redirect('index')
       context = {
           'form':form
       }
       return render(request,'templates/ambulance_forms.html',context)
  

def conformationToDeleteAmbulance(request,pk):
      data = ambulance.objects.get(pk=pk)
      context ={
        'data':data
      }
      return render(request,'templates/conformAmbulance.html',context)
def deleteAmbulance(request,pk):
      ambulance = ambulance.objects.get(pk=pk)
      ambulance.delete()
      messages.success(request,'Ambulance has been Deleted!')
      return redirect('home')

@api_view()
def get_CurrentLocationAmbulance(request):
      queryset = ambulanceCurrentLocation.objects.all()
      serializer  =AmbulanceCurrentLocationSerializer(queryset,many=True)
      return Response({
            "data":serializer.data
      })


class AmbulancesApi(APIView):
      def get(self,request):
             queryset = ambulance.objects.all()
             serializer=AmbulanceSerializer(queryset,many=True)
             return Response({
                 "data":serializer.data
               })
      def post(self,request):
            dataAmb = request.data
            serializer = AmbulanceSerializer(data=dataAmb)
            if not serializer.is_valid():
                  return Response({
                        "message":"Data is invalid",
                        "errors":serializer.errors,
                  })
            serializer.save()

            return Response({
                  "message":"Data Saved",
                  "data":serializer.data,
            })

      def put(self,request):
            return Response({
                  "message":"this is a put method for api"
            })
      def patch(self,request):
            data = request.data
            if not data.get('amid'):
                  return Response({
                        "message":"Data not updated",
                        "errors":"id is invalid",
                  })
            ambulanceData = ambulance.objects.get(amid=data.get('amid'))
            serializer=AmbulanceSerializer(ambulanceData,data=data,partial=True)
            if not serializer.is_valid():
                  return Response({
                        "message":"Data is invalid",
                        "errors":serializer.errors,
                  })
            serializer.save()
     
            return Response({
                  "message":"Data Saved",
                  "data":serializer.data,
            })
      def delete(self,request):
             data = request.data
             if not data.get('curAmb'):
                   return Response({
                         "message":"Data not updated",
                         "errors":"id is invalid",
                   })
             ambulanceCurrentLocaData = ambulance.objects.get(curAmb=data.get('amid')).delete()
             
             return Response({
                   "message":"Data Delete",
                   "data":{},
             })
      





class UserAmbulancesApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_ambulances = ambulance.objects.filter(ambulanceDriverName=user) | ambulance.objects.filter(ambulanceDriver2Name=user)
        serializer = AmbulanceSerializer(user_ambulances, many=True)
        return Response({"data": serializer.data})
    
    
class AmbulanceCurrentLocationApi(APIView):
      def get(self,request):
             queryset = ambulanceCurrentLocation.objects.all()
             serializer=AmbulanceCurrentLocationSerializer(queryset,many=True)
             return Response({
                 "data":serializer.data
               })
      def post(self,request):
            dataAmbCur = request.data
            serializer = AmbulanceCurrentLocationSerializer(data=dataAmbCur)
            if not serializer.is_valid():
                  return Response({
                        "message":"Data is invalid",
                        "errors":serializer.errors,
                  })
            serializer.save()

            return Response({
                  "message":"Data Saved",
                  "data":serializer.data,
            })

      def put(self,request):
            return Response({
                  "message":"this is a put method for api"
            })
      def patch(self,request):
            data = request.data
            if not data.get('curAmb'):
                  return Response({
                        "message":"Data not updated",
                        "errors":"id is invalid",
                  })
            ambulanceCurrentLocaData = ambulanceCurrentLocation.objects.get(curAmb=data.get('curAmb'))
            serializer=AmbulanceCurrentLocationSerializer(ambulanceCurrentLocaData,data=data,partial=True)
            if not serializer.is_valid():
                  return Response({
                        "message":"Data is invalid",
                        "errors":serializer.errors,
                  })
            serializer.save()
     
            return Response({
                  "message":"Data Saved",
                  "data":serializer.data,
            })
      def delete(self,request):
             data = request.data
             if not data.get('curAmb'):
                   return Response({
                         "message":"Data not updated",
                         "errors":"id is invalid",
                   })
             ambulanceCurrentLocaData = ambulanceCurrentLocation.objects.get(curAmb=data.get('curAmb')).delete()
             
             return Response({
                   "message":"Data Delete",
                   "data":{},
             })
      

class NotificationApi(APIView):
      def get(self,request):
             queryset = Notification.objects.all()
             serializer=NotificationSerializer(queryset,many=True)
             return Response({
                 "data":serializer.data
               })
      def post(self,request):
            dataNoti = request.data
            serializer = NotificationSerializer(data=dataNoti)
            if not serializer.is_valid():
                  return Response({
                        "message":"Data is invalid",
                        "errors":serializer.errors,
                  })
            serializer.save()

            return Response({
                  "message":"Data Saved",
                  "data":serializer.data,
            })

      def put(self,request):
            return Response({
                  "message":"this is a put method for api"
            })
      def patch(self,request):
            data = request.data
            if not data.get('curAmb'):
                  return Response({
                        "message":"Data not updated",
                        "errors":"id is invalid",
                  })
            notification = Notification.objects.get(notid=data.get('notid'))
            serializer=NotificationSerializer(notification,data=data,partial=True)
            if not serializer.is_valid():
                  return Response({
                        "message":"Data is invalid",
                        "errors":serializer.errors,
                  })
            serializer.save()
     
            return Response({
                  "message":"Data Saved",
                  "data":serializer.data,
            })
      def delete(self,request):
             data = request.data
             if not data.get('notid'):
                   return Response({
                         "message":"Data not updated",
                         "errors":"id is invalid",
                   })
             notify = Notification.objects.get(notid=data.get('notid')).delete()
             
             return Response({
                   "message":"Data Delete",
                   "data":{},
             })
      

class CustomUserApi(APIView):
      def get_permissions(self):
        if self.request.method in ['POST']:
            return [AllowAny()]  # Allow anyone to register
        elif self.request.method in ['GET', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]  # Require login for sensitive actions
        else:
            return [IsAuthenticated()] 
      
      def get(self,request):
             if not request.user.is_authenticated:
                   return Response("Invalid Credentials")
             
             user = request.user
             queryset = CustomUser.objects.all()
             serializer=CustomUserSerializer(queryset,many=True)
             return Response({
                 "data":serializer.data
               }) 
      def post(self,request):
            dataNoti = request.data
            serializer = CustomUserSerializer(data=dataNoti)
            if not serializer.is_valid():
                  return Response({
                        "message":"Data is invalid",
                        "errors":serializer.errors,
                  })
            serializer.save()

            return Response({
                  "message":"Data Saved",
                  "data":serializer.data,
            })

      def put(self,request):
            return Response({
                  "message":"this is a put method for api"
            })
      def patch(self,request):
            data = request.data
            if not data.get('id'):
                  return Response({
                        "message":"Data not updated",
                        "errors":"id is invalid",
                  })
            notification = CustomUser.objects.get(id=data.get('id'))
            serializer=CustomUserSerializer(notification,data=data,partial=True)
            if not serializer.is_valid():
                  return Response({
                        "message":"Data is invalid",
                        "errors":serializer.errors,
                  })
            serializer.save()
     
            return Response({
                  "message":"Data Saved",
                  "data":serializer.data,
            })
      def delete(self,request):
             data = request.data
             if not data.get('id'):
                   return Response({
                         "message":"Data not updated",
                         "errors":"id is invalid",
                   })
             user = CustomUser.objects.get(notid=data.get('notid')).delete()
             
             return Response({
                   "message":"Data Delete",
                   "data":{},
             })
      
 

class UserLoginView(APIView):
      def get_permissions(self):
        if self.request.method in ['POST']:
            return [AllowAny()]  # Allow anyone to register
        elif self.request.method in ['GET', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]  # Require login for sensitive actions
        else:
            return [IsAuthenticated()] 
      



      def get(self,request):
             if not request.user.is_authenticated:
                   return Response("Invalid Credentials")
             
             user = request.user
            #  queryset = CustomUser.objects.all()
             serializer=CustomUserSerializer(user.email,many=True)
             return Response({
                 "data":serializer.data
               }) 
      def post(self,request):
            print("login")
            data = request.data
            print(data)
            user_data = CustomUser.objects.get(email=data.get('email'))
            print(user_data.email)
            if user_data is not None:
                  credentials = {
                        'lemail':user_data.email,
                        'lpassword':data.get('password')
                  }
                  user = authenticate(email=credentials["lemail"],password=credentials["lpassword"])

                  print(user)
                  if user and user.is_active:
                        user_serializer = CustomUserSerializer(user)
                        return Response(user_serializer.data,status=200)

            return Response("Invalid Credentials",status=403)
      
      