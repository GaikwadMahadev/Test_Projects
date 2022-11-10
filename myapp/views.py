from django.shortcuts import render
from django.http import HttpResponse
from .models import Job

# Create your views here.

def home(request):
    if request.method == 'GET':
        data = Job.objects.all()

    # return HttpResponse("Hi this is my Home Page")
        return render(request,'myapp/home.html',{'data':data})