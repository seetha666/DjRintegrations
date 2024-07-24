from django.shortcuts import render
from api.models import Employee
from api.serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
        operation_description="Retrieve an example item",
        responses={200: openapi.Response('Description', EmployeeSerializer)}
    )
class EmployeeViewL(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
