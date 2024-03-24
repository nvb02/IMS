from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet #to be used to transform a class into an API view.
from .models import * #importing everything from models.py into views.py
from rest_framework.decorators import api_view #decorators allows a function to be run before the other function.
from .serializers import * #calling departmentserializer from serializers.py for conversion of objects into json and vice-versa.

# Create your views here.

# @api_view()
# def department(request): #the api_view decorator converts the department function into API function based view but not using the @api_view() will let this function to stay normal in which front-end cannot request. this is another method to form API view class but here, all the CRUD logics must be defined and logics related to authentication, filters, permission are difficult to define in this view which is easy to define in class based views.


class DepartmentView(ModelViewSet): # inheriting imported ModelViewSet into normal DepartmentView class to convert it into an API View Class, any project from front-end not necessarily django can now request this view and run CRUD Operations (in this class, data control operation) giving flexibility to companies incase of alterations of front-end.
    queryset = Department.objects.all() #there are other ways to make API view class but when ModelViewSet is inherited to make API class, queryset variable must be defined. queryset enables or allows CRUD operation to be performed on the department table and all of its components. define "objects.all" to the model or table where CRUD operation needs to be performed where CRUD methods or logics are already predefined. the name 'queryset' must be defined as it is because ModelViewSet calls this object from its defined methods which is why spelling errors and pascal case must be considered.
    serializer_class = DepartmentSerializer #defining serializer_class variable where DepartmentSerializer will convert Department model object into json, and the json data coming from request is converted into object through this serializer for this model.
    
class ResourceView(ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    
class EmployeeProfileView(ModelViewSet):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer
    
class VendorView(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
class PurchaseView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    
    
    