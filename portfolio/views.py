from django.shortcuts import render # type: ignore
from .models import Project #import class from models.py

# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html',{'projects':projects})
  