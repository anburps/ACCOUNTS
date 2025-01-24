from django.shortcuts import render
from django_rest_framework import from django.views.generic import CreateView
# Create your views here.
def index(request):
    return render(request,'index.html')