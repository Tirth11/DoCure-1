from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required



from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *


def home(request):
    	 return render(request,'accounts/home.html')

from .models import Contact


def registerPage(request):
	
		
		if request.method == 'POST':
			name=request.POST['name']
			email=request.POST['email']
			age=request.POST['age']
			gender=request.POST['gender']
			# weight=request.POST['weight']
			password=request.POST['password']
			# password2=request.POST['password2']
			# print(name,email)
			ins=Contact(name=name,email=email,age=age,gender=gender,password=password)
			ins.save()
			return render(request, 'accounts/login.html')
		return render(request, 'accounts/register.html')
		
def loginPage(request):
		if request.method == 'POST':
			username = request.POST.get('name')
			password =request.POST.get('password')

			user = authenticate(request, name=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)


