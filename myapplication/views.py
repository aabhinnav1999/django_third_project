from django.shortcuts import render,HttpResponse
from .models import student

# Create your views here.
def samp1(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname'] 
        dept=request.POST['dept'] 
        age=request.POST['age'] 
        # print(first_name,last_name,dept,age)
        student.objects.create(first_name=first_name.upper(),last_name=last_name.upper(),dept=dept.upper(),age=age)
        return render(request,'submit.html')
    return render(request,'index.html')