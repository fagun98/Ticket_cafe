from django.shortcuts import render
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .models import Username
from .forms import *

def userindex(request):
    return render(request,'username_form.html')

def UserCreate(request):
    if request.method == 'POST':
        username = UC(request.POST);
        if username.is_valid:
           username.save();
        return render(request,'ticket/logged.html')

    if request.method=='GET':
        username = UC();
        return render(request,'test_forms/username_form.html',{'form':username})
    
    


