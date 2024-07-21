from django.urls import path,include
from api import views
from rest_framework import routers
Router=routers.DefaultRouter()
Router.register('employees',views.EmployeeViewL)
urlpatterns = [
    path('',include(Router.urls)),
]
