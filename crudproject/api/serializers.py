from rest_framework import serializers #if we are not getting this in problem section goto environmentsinterpreter and select it
from api.models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
   class Meta:
    model=Employee
    fields=['id','name','number','email','mobile','address']
    