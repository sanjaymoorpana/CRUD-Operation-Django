from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def home(request):
    employees = Employee.objects.all()
    return render(request,'home.html',{'employees':employees})

def add(request):
    if request.method == "POST":
        form = EmployeeForm(data=request.POST)  
        if form.is_valid:
            form.save()
            return render(request,'home.html',{'form':form})
        
    else:
        form = EmployeeForm()
        return render(request,'add.html',{'form':form})

def edit(request,id):
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeForm(instance=employee,data=request.POST)
        print("DATA")
        if form.is_valid:
            form.save()
            return redirect('home')

    else:
        form = EmployeeForm(instance=employee)
        return render(request,'edit.html',{'form':form,'employee':employee})

def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('home')