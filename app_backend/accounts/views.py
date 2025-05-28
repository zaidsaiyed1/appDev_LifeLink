from datetime import datetime
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.conf import settings
from core.models import *
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import *
# Create your views here.

def send_mail_to_companyadmin(request,semail,password):
          subject = "Your Admin Panel Credential for Quiz Management"
          message = f"""Hello,\nThis mail has your username and password for login in your Quiz Management Control Panel
          \nusername:{semail}\npassword:{password}
          \nPlease don't share this mail/credentials with anyone!\nHave a good day!"""
          from_email = settings.EMAIL_HOST_USER
          recipient_list  = [semail]
          send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)
          return redirect('index')


def register(request):
  form = UserRegisterationForm()
  if request.method == 'POST':
    form = UserRegisterationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('email')
      messages.success(request,'Account has been created '+username)
      return redirect('login')
  else:
    form = UserRegisterationForm()
  context ={
    'form':form
  }
  return render(request,'templates/registeration/register.html',context)

def editdata(request,email):
  userdata = CustomUser.objects.get(email=email)
  form = UserRegisterationForm(instance=userdata)
  if request.method == 'POST':
    form = UserRegisterationForm(request.POST,request.FILES,instance=userdata)
    if form.is_valid():
      form.save()
      messages.success(request,"Data Has been Updated!")
      return redirect('index')
  
  context ={
    'form':form,
    'userdata':userdata,
  }
  return render(request,'templates/registeration/editprofile.html',context)

def deleteUser(request,email):
  data = CustomUser.objects.get(email=email)
  data.delete()
  messages.success(request,"User Has been Deleted!")
  return redirect('index')

def comformUserDelete(request,email):
  data = CustomUser.objects.get(email=email)
  context = {
    'data':data
  }
  return render(request,'templates/registeration/conformUser.html',context)

def registerForManager(request):
  is_adminSite = False
  user = request.user.email
  if CustomUser.objects.filter(email=user).exists():
    is_adminSite = True
  form = UserRegisterationFormForOrganizerManager()
  if request.method == 'POST':
    form = UserRegisterationFormForOrganizerManager(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('email')
      password = form.cleaned_data.get('password1')
      messages.success(request,'Account has been created '+username)
      send_mail_to_companyadmin(request,username,password)
      return redirect('login')
  else:
    form = UserRegisterationFormForOrganizerManager ()
  context ={
    'form':form,
    'is_adminsite':is_adminSite
  }
  return render(request,'templates/registeration/registerForManager.html',context)

def loginhandle(request):
   if request.method == 'POST':
     lusername = request.POST['email']
     lpassword = request.POST['password']
     loginuser = authenticate(email=lusername,password=lpassword)
     if loginuser is not None:
        if loginuser.is_driver == True and loginuser.is_Gov_Official == False and loginuser.is_ambulanceOrganizer_Person==False:
           if loginuser.is_order==False:
             login(request,loginuser)
             data = CustomUser.objects.get(email=lusername)
             data.is_student = False
             data.save()
             messages.success(request,'Logged In Successfully ' + lusername)
             return redirect('plansForQuiz')
          #  elif loginuser.is_order==True:
          #   data = Order.objects.get(user=loginuser)
          #   if data.checkUserOrderExpire():
          #     messages.warning(request,'Your Plans Is expired! Re-Login!')
          #     data.delete()
          #     loginuser.is_order = False
          #     loginuser.save()  
          #     return redirect('login')
           else:
              login(request,loginuser)
              messages.success(request,'Logged In Successfully ' + lusername)
              return redirect('controlPanelForQuizManage')
            
        elif loginuser.is_docsManager == True and loginuser.is_quizManager == False:
          login(request,loginuser)
          messages.success(request,'Logged In Successfuly ' + lusername)
          return redirect('controlPanelForQuizManage') 
        else:
          login(request,loginuser)
          messages.success(request,'Logged In Successfully ' + lusername)
          return redirect('index')
     else:
        messages.error(request,lusername+' Invalid Credentials!')
        return redirect('login')
     
   context ={
   
  }
   return render(request,'templates/registeration/login.html',context)

def profileData(request,email):
   userdata = CustomUser.objects.get(email=email)
   context = {
      'userdata':userdata
   }
   return render(request,'templates/registeration/profile.html',context)
def logouthandle(request):
   logout(request)
   messages.success(request,'Logout Sucessfully')
   return redirect('index')

