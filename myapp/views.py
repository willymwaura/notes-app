from django.contrib.messages.api import info
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Feature
from django.contrib.auth.models import User, UserManager,auth
from django .contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
     queryset=Feature.objects.all()
     return render(request,"index.html",{"object_list":queryset})

def counter(request):
    words=request.POST["text"]
    words=len(words.split())
    return render(request,"counter.html",{"amount": words})

def register(request):
     if request.method=="POST":
          form=UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               username=form.cleaned_data.get("username")
               messages.info(request," account created ")
               return redirect("index.html")
          else:
               return render(request,"register.html",{"form":form})
               
     
     
     else:
           form=UserCreationForm()
           return render (request,"register.html",{"form":form})
 
    
