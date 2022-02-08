from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms  import NewUserForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from django.contrib import messages

from django.contrib.auth.decorators import login_required

import re
# import requests
import pdfplumber
import pandas as pd


# Create your views here.
from .models import *


def home(request):
	name=request.user.username or None
	return render(request,'accounts/home.html',{'name':name})

def about(request):
	return render(request,'accounts/about.html')

def dashboard(request):
	return render(request,'accounts/dashboard.html')

# def sign(request):
    	

# 			if request.method == 'POST':
# 				age=request.POST['age']
# 				gender=request.POST['gender']
# 				ins=Contact(age=age,gender=gender)
# 				ins.save()
# 				return render(request, 'accounts/login.html')

def registerPage(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request,context={'register_form':form} ,template_name='accounts/register.html')


	

def extract(text):
    wbc_re = re.compile(r'(.*[Ll]eu[ck]ocyte.*|.*WBC.*|.*White Blood Cell.*) ([\d,.]+) ')
    rbc_re = re.compile(r'(.*[eE]rythrocyte.*|.*[r,R][b,B][c,C].*|.*[Rr]ed [Bb]lood [Cb]ell.*|.*[Rr]ed [Cc]ell [Cc]ount.*) ([\d,.]+) ')
    hgb_re = re.compile(r'(.*[Hh][a]*emoglobin.*) ([\d,.]+) ')
    pcv_re = re.compile(r'(.*[Pp]acked [Cc]ell [Vv]olume.*|.*[pP][cC][vV].*|.*[Hh][a]*ematocrit) ([\d,.]+) ')
    mcv_re = re.compile(r'(.*[Mm]ean [Cc]orpuscular [Vv]olume.*|.*[mM][cC][vV].*) ([\d,.]+) ')
    mch_re = re.compile(r'(.*[Mm]ean [Cc]orpuscular [Hh]b.*|.*[mM][cC][hH].*) ([\d,.]+) ')
    mchc_re = re.compile(r'(.*[Mm]ean [Cc]ell [Hh]b Conc.*|.*[mM][cC][hH][cC].*) ([\d,.]+) ')
    rcd_re = re.compile(r'(.*[Rr]ed [Cc]ell [Dd]ist.*|.*[Rr][cC][Dd].*|.*[Rr][Dd][Ww].*) ([\d,.]+) ')
    pc_re = re.compile(r'(.*[Pp]la[Ee]*telet [Cc]ount.*) ([\d,.]+) ')
    mpv_re = re.compile(r'(.*[Mm]ean Pla[eE]*telet [Vv]olume.*|.*[Mm][Pp][Vv].*) ([\d,.]+) ')
#     neu_re = re.compile(r'([Nn]eutrophils) ([\d,.]+) ')
#     lym_re = re.compile(r'(.*[Ll]ymphocyte.*) ([\d,.]+) ')
#     mon_re = re.compile(r'(.*[Mm]onocyte.*) ([\d,.]+) ')
#     eos_re = re.compile(r'(.*[Ee]osinophils.*) ([\d,.]+) ')
#     bas_re = re.compile(r'(.*[Bb]asophils.*) ([\d,.]+) ')
    
    flag = 0
    
    wbc = wbc_re.search(text)
    if(wbc != None):
        wbc = wbc_re.search(text).group(2)
        wbc = float(wbc.replace(',',''))
        if(wbc>1000 and wbc<100000):
            wbc /= 1000
    else:
        wbc = "Not Available"
        flag += 1
        
    rbc = rbc_re.search(text)
    if(rbc != None):
        rbc = rbc_re.search(text).group(2)
        rbc = float(rbc.replace(',',''))
    else:
        rbc = "Not Available"
        flag += 1
        
    hgb = hgb_re.search(text)
    if(hgb != None):
        hgb = hgb_re.search(text).group(2)
        hgb = float(hgb.replace(',',''))
    else:
        hgb = "Not Available"
        flag += 1
        
    pcv = pcv_re.search(text)
    if(pcv != None):
        pcv = pcv_re.search(text).group(2)
        pcv = float(pcv.replace(',',''))
    else:
        pcv = "Not Available"
        flag += 1
        
    mcv = mcv_re.search(text)
    if(mcv != None):
        mcv = mcv_re.search(text).group(2)
        mcv = float(mcv.replace(',',''))
    else:
        mcv = "Not Available"
        flag += 1
        
    mch = mch_re.search(text)
    if(mch != None):
        mch = mch_re.search(text).group(2)
        mch = float(mch.replace(',',''))
    else:
        mch = "Not Available"
        flag += 1
        
    mchc = mchc_re.search(text)
    if(mchc != None):
        mchc = mchc_re.search(text).group(2)
        mchc = float(mchc.replace(',',''))
    else:
        mchc = "Not Available"
        flag += 1
        
    rcd = rcd_re.search(text)
    if(rcd != None):
        rcd = rcd_re.search(text).group(2)
        rcd = float(rcd.replace(',',''))
    else:
        rcd = "Not Available"
        flag += 1
        
    pc = pc_re.search(text)
    if(pc != None):
        pc = pc_re.search(text).group(2)
        pc = float(pc.replace(',',''))
    else:
        pc = "Not Available"
        flag += 1
        
    mpv = mpv_re.search(text)
    if(mpv != None):
        mpv = mpv_re.search(text).group(2)
        mpv = float(mpv.replace(',',''))
    else:
        mpv = "Not Available"
        flag += 1
        
    if(flag > 5):
        print("Could not find values. Please check if the correct report is uploaded.")
    else:
        print("Leukocyte count: ", wbc)
        print("Red Blood Cell count: ", rbc)
        print("Haemoglobin Count: ", hgb)
        print("Packed Cell Volume: ", pcv)
        print("Mean Cell Volume: ", mcv)
        print("Mean Corpuscular Hb Conc.: ", mchc)
        print("Red Cell Dist.: ", rcd)
        print("Platelet Count: ", pc)
        print("Mean Platelet Volume: ", mpv)

    return rbc, wbc, pc

        

    	

def GetInfo(path):
    cbc = path
    with pdfplumber.open(cbc, password='9821714272') as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
    rbc, wbc, pc = extract(text)
    return rbc, wbc, pc


def FILE(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        print(uploaded_file)
        rbc, wbc, pc = GetInfo(uploaded_file)
        user = request.user.get_username()

        cbc = Cbc()
        cbc.user = request.user
        cbc.rbc = rbc
        cbc.wbc = wbc
        cbc.pc = pc
        cbc.save()

        

    return render(request, 'accounts/FILE.html', context)


def loginPage(request):
		if request.method == 'POST':
			username = request.POST.get('name')
			password =request.POST.get('password') 



			user = authenticate(request,username=username,password=password)
			if user is not None:
				
					login(request, user)
					
					return redirect('home')
			else:
					messages.success(request,"there was error")
					
	
		return render(request, 'accounts/login.html')

def logout_view(request):
		logout(request)
		messages.info(request, "You have successfully logged out.") 
		return redirect("login")


