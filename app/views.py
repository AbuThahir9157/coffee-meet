from django.shortcuts import render
from django.http import HttpResponse
from . models import Cofeee

def home(request):

    cofeee=Cofeee.objects.all()
    return render(request,'home.html',{'cofeee':cofeee})
