from django.db import models
class empTable(models.Model):
    Employee_ID=models.IntegerField(primary_key=True)
    Employee_Name=models.CharField(max_length=20)
    Employee_Salary=models.IntegerField()
    Address=models.CharField(max_length=20)
    def __str__(self):
        return str(self.Employee_ID)+' ---> '+self.Employee_Name