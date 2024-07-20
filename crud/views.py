from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Candidate
# Create your views here.
def register_view(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    data=Candidate.objects.all()
    return render(request,'dashboard.html',{'data':data})

@login_required
def create(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        job=request.POST['job']
        salary=request.POST['salary']
        obj=Candidate.objects.create(name=name,age=age,address=address,job=job,salary=salary)
        return redirect('dashboard')
    
@login_required
def update(request,id):
    data=Candidate.objects.get(id=id)
    if request.method=="POST":
        data.name=request.POST['name']
        data.age=request.POST['age']
        data.address=request.POST['address']
        data.job=request.POST['job']
        data.salary=request.POST['salary']
        data.save()
        return redirect('dashboard')
    return render(request,'update.html',{'data':data})

@login_required
def delete(request,id):
    data=Candidate.objects.get(id=id)
    data.delete()
    return redirect('dashboard')
        