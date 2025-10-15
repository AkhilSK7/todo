from django.shortcuts import render,redirect
from django.views import View
from users.forms import Signupform,Loginform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Register(View):
    def get(self,request):
        form_instance=Signupform()
        context={'form':form_instance}
        return render(request,'register.html',context)
    def post(self,request):
        form_instance=Signupform(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users:login')
        else:
            return render(request,'register.html',{'form':form_instance})
class Login(View):
    def get(self,request):
        form_instance=Loginform()
        context={'form':form_instance}
        return render(request,'login.html',context)
    def post(self,request):
        form_instance=Loginform(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']
            user=authenticate(username=u,password=p)
            if user:
                login(request,user)
                return redirect('app1:home')
            else:
                messages.error(request,"Invalid user credentials")
                return redirect('users:login')

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('users:userhome')