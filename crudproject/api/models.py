from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=50)
    number=models.IntegerField()
    email=models.EmailField()
    mobile=models.BigIntegerField()
    address=models.CharField(max_length=100)
