from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import empTable
from .forms import empForm
def home(request):
    return render(request,'home.html')
def display(request):
    context=empTable.objects.all()
    return render(request,'display.html',{'context':context})
def insert(request):
    form=empForm()
    if request.method=='POST':
        form=empForm(request.POST)
        if form.is_valid():
            Emp_No=form.cleaned_data['Emp_No']
            Emp_Name=form.cleaned_data['Emp_Name']
            Emp_Salary=form.cleaned_data['Emp_Salary']
            Emp_Address=form.cleaned_data['Emp_Address']
            g=empTable(Emp_No,Emp_Name,Emp_Salary,Emp_Address)
            g.save()
            return HttpResponseRedirect('../display')
    return render(request,'insert.html',{'form':form})
def update(request,id):
    employee = empTable.objects.get(Employee_ID=id)
    if request.method == "POST":
        form = empForm(request.POST)
        if form.is_valid():
            Emp_No=form.cleaned_data['Emp_No']
            Emp_Name=form.cleaned_data['Emp_Name']
            Emp_Salary=form.cleaned_data['Emp_Salary']
            Emp_Address=form.cleaned_data['Emp_Address']
            g=empTable(Emp_No,Emp_Name,Emp_Salary,Emp_Address)
            g.save()
            return HttpResponseRedirect('../../display')
    else:
        form = empForm(initial={'Emp_No': employee.Employee_ID, 'Emp_Name': employee.Employee_ID, 'Emp_Salary':employee.Employee_Salary, 'Emp_Address':employee.Address})
    return render(request, "update.html", {"form": form})
def delete(request,id):
    g=empTable.objects.filter(Employee_ID=id)
    g.delete()
    return HttpResponseRedirect('../../display')