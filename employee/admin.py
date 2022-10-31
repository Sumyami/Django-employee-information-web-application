from django.contrib import admin
from .models import empTable
@admin.register(empTable)
class empAdmin(admin.ModelAdmin):
    list_display=('Employee_ID','Employee_Name','Employee_Salary')
    list_filter=('Employee_ID',)
    ordering=('Employee_ID',)
    search_fields=('Employee_Name',)