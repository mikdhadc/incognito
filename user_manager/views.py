from django.shortcuts import render
from user_manager.forms import LoginForm, RegisterForm
from django.views import View
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

class LoginView(View):

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            print("request.user ->", request.user)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if(user):
                login(request, user)
                print("request.user ->", request.user)
            return HttpResponseRedirect('/msg_manager/view/')
        else:
            return render(request, 'login.html', {'form':form})
    
   
    def get(self, request):
            form = LoginForm()
            return render(request, 'login.html',{'form':form})
    

class RegisterView(View):
    def get(self,request):
        form2 = RegisterForm()
        return render(request, 'register.html', {'form2':form2})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        usercreate = User.objects.create(username=username, password=password, email=email)
        return render(request, 'response.html',{'username':username})