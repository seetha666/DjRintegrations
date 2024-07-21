from django.contrib import admin
from api.models import Employee
@admin.register(Employee)
class EmpAdmin(admin.ModelAdmin):
    list_display=['id','name','number','email','mobile','address']
