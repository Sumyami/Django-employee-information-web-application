from django import forms
class empForm(forms.Form):
    Emp_No=forms.IntegerField()
    Emp_Name=forms.CharField(max_length=20)
    Emp_Salary=forms.IntegerField()
    Emp_Address=forms.CharField(max_length=20)