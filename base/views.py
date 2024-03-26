from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet #to be used to transform a class into an API view.
from .models import * #importing everything from models.py into views.py
from rest_framework.generics import GenericAPIView # a view class that must be inherited to convert normal class into api view class where logics should be written manually.
from rest_framework.decorators import api_view #decorators allows a function to be run before the other function.
from .serializers import * #calling all the serializers from serializers.py for conversion of objects into json and vice-versa.
from rest_framework.response import Response #importing response class from response module of rest_framework API to send response using GenericAPIView
from rest_framework import status #importing status module from rest framework to include status wherever necessary manually.
# Create your views here.

# @api_view()
# def department(request): #the api_view decorator converts the department function into API function based view but not using the @api_view() will let this function to stay normal in which front-end cannot request. this is another method to form API view class but here, all the CRUD logics must be defined and logics related to authentication, filters, permission are difficult to define in this view which is easy to define in class based views.


class DepartmentView(ModelViewSet): # inheriting imported ModelViewSet into normal DepartmentView class to convert it into an API View Class, any project from front-end not necessarily django can now request this view and run CRUD Operations (in this class, data control operation) giving flexibility to companies incase of alterations of front-end.
    queryset = Department.objects.all() #there are other ways to make API view class but when ModelViewSet is inherited to make API class, queryset variable must be defined. queryset enables or allows CRUD operation to be performed on the department table and all of its components. define "objects.all" to the model or table where CRUD operation needs to be performed where CRUD methods or logics are already predefined. the name 'queryset' must be defined as it is because ModelViewSet calls this object from its defined methods which is why spelling errors and pascal case must be considered.
    serializer_class = DepartmentSerializer #defining serializer_class variable where DepartmentSerializer will convert Department model object into json, and the json data coming from request is converted into object through this serializer for this model.
    
class ResourceView(GenericAPIView): #converting resourceview class into api view class through GenericAPIView
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    
    def get(self,request): # defining get method or function for the get request manually as no modelviewset is used. "self" parameter is compulsory on the method defined under a class. Since url will call this method, "request" parameter must be included for request and response cycle.
        queryset = self.get_queryset() # get_queryset method is defined in GenericAPIView if queryset object is defined in the class, get_queryset method calls the query from the queryset object. 
        serializer = self.serializer_class(queryset, many = True) #making serializer variable that calls the serializer_class object or attribute. passing queryset which is object data as a positional argument inside the serializer_class to be converted into JSON and many=true states that the conversion takes place on more than one object by using for loop, i.e list of objects that lies in queryset.
        return Response(serializer.data) #data is a property or method that does not require paranthesis which returns the converted JSON data of queryset object through the url in the form of response. response is imported from response module of rest framework API.
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data) #the JSON data coming from request data is converted into object by using serializer (to create data in the resource model). the JSON data is passed into the data parameter, ie (data=request.data) and serializer object is created where JSON data is passed.
        if serializer.is_valid(): #the data sent should be checked if the value matches the nature and the required fields of the model by running the is_valid() method. if data is valid, it returns true otherwise it returns false incase of invalid or missing data.
            serializer.save() #JSON data gets converted to object and serializer queries the database to create the object on resource model.
            return Response('Data Created!') #showing string response to the front-end regarding creation of data. this is an Http data as it is a string data (not a json data)
        else:
            return Response(serializer.errors) #to show errors of the JSON data after being checked by is_valid() method to the front-end due to mismatching or missing data in the model fields. error message is created by the serializer itself.
        
class ResourceDetailView(GenericAPIView): #creating a new class to define the functions of update, delete or get a specific ID of a model. 
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
          
    def get(self,request,pk): # making a different get function for get single retrieve. specific ID from url gets assigned to pk that gets passed to this get method in the url sent by the front-end user. not adding pk parameter can show error.
        try: #using try statement to eliminate exception error of 500 internal server error when client sends improper request.
            queryset = Resource.objects.get(id=pk) #bringing a single data from the db with the help of pk where the id of data = pk sent by the front end according to the keyword argument (id=pk). id is an automatically created field (primary key) made in the resource model. we use id field because it is a unique identifier of data.
        except:
            return Response('Data Not found!', status=status.HTTP_404_NOT_FOUND) #incase of failure to acheive the try statement of getting the data from db, response is sent to the front-end of no data found in order to prevent internal server error 500, the content of the response should match the status of the response displayed hence, 200 OK is not appropriate in this page because no data was found, so 404 not found status should be displayed which is fetched from the status module of the rest framework. we change the default status of 200 OK to 404 not found!
        serializer = self.serializer_class(queryset)  #converting the object from the db to a JSON file to be sent to front user
        return Response(serializer.data) #data method returns the JSON file to the client as a response through the url.
    
    def put(self,request,pk): #to update a specific data in the db by front-end.
        try:
            queryset = Resource.objects.get(id=pk)
        except:
            return Response('Data Not found!', status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(queryset, data=request.data) #request.data defines that the JSON data from the client is to be converted into object data, the changed data is then updated in the queryset object. so to update data, we use serializer class by passing the first parameter as the object to be changed and the 2nd parameter should be data that includes the data to be passed to the object.
        if serializer.is_valid(): #checking if the sent data matches the requirement of the fields of model
            serializer.save() #saving if the data matches with the models fields.
            return Response('Data updated!')
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        try:
            queryset = Resource.objects.get(id=pk)
        except:
            return Response('Data Not found!', status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response('Data deleted!')
        
            
            
# class ResourceView(ModelViewSet):
#     queryset = Resource.objects.all()
#     serializer_class = ResourceSerializer
    
class EmployeeProfileView(ModelViewSet):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer
    
class VendorView(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
class PurchaseView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    
    
    