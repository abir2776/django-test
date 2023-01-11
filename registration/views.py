from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
#Authetication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .forms import SignUpForm

#Messages

from django.contrib import messages
# Create your views here.
def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully!")
            return HttpResponseRedirect('login')
    return render(request,'registration/registration.html',context={'form':form})

def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                #return HttpResponseRedirect(reverse('app_shop:home'))

    return render(request,'registration/login.html',context={'form':form})
