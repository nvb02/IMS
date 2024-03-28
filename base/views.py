from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet #to be used to transform a class into an API view.
from .models import * #importing everything from models.py into views.py
from rest_framework.generics import GenericAPIView # a view class that must be inherited to convert normal class into api view class where logics should be written manually.
from rest_framework.decorators import api_view #decorators allows a function to be run before the other function. used in the login function to allow it to become a part of API view.
from rest_framework.decorators import permission_classes #to define permissions to the API class. in this case, using it in login function.
from .serializers import * #calling all the serializers from serializers.py for conversion of objects into json and vice-versa.
from rest_framework.response import Response #importing response class from response module of rest_framework API to send response using GenericAPIView
from rest_framework import status #importing status module from rest framework to include status wherever necessary manually.
from rest_framework.permissions import IsAuthenticated #permission module in rest framework contains information related to API permissions such as only user that has logged in can gain permission to the API, permissions according to the type of logged in user, IsAuthenticated class from permissions module allows only logged in or authenticated user to make requests.
from django.contrib.auth import authenticate #auth module of django consists of all aspects of authentication such as user table, group, permissions etc. authenticate function of this module helps to verify the email and password provided by the user to check if the user is an authenticated user.
from rest_framework.authtoken.models import Token #importing token table from authtoken app that has stored tokens for users.
from rest_framework.permissions import AllowAny #AllowAny permission class gives access to anyone neglecting the need for a valid or authenticated user. this is imported to be used in the login API since all the other APIs have IsAuthenticated class logic.
from django.contrib.auth.hashers import make_password #make password function to encrypt the password to store during registration

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
    #permission_classes = [IsAuthenticated] #this attribute is already defined in genericapiview, isauthenticated checks whether credentials is sent from the user in front-end and also checks whether requesting user is from the user table, 
          
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
    
@api_view(['POST']) 
@permission_classes([AllowAny,]) 
def register(request): # a user needs to be registered to experience a successful login. we create a user data in the user table.
    
    serializer = UserSerializer(data=request.data) #email and password is sent to the request from front-end which is passed to the serializer
    if serializer.is_valid(): #validation is necessary specially incase for emails as it needs to be unique. the given valid method checks whether the value is sent to the required field or not, and whether the nature of value matches the field value or not. incase for unique=true, it also checks for duplicacy.
        password = request.data.get('password') #getting the value of password which is not encrypted from the password key on the request data.
        hash_password = make_password(password) #make_password encrypts the password and returns it to the "hash_password" variable. 
        a = serializer.save() #if data is valid, save function creates the data and assigns the saved data as an object to variable 'a'.
        a.password = hash_password #changing the unencrypted serialized password stored in 'a' variable to hash_password (encrypted password)
        a.save() #saving the 'a' variable to the db.
        return Response('User created!') #response to front-end.
    else: #if data sent is not valid
        return Response(serializer.errors) #sending error message occured to the front-end.
        
    
@api_view(['POST']) #a decorator with parameter "POST" method to post the email and password sent by the front-end.
@permission_classes([AllowAny,]) #when request is made to the login API, the AllowAny class of permission is run making the API accessible to any user without validity. the default permission class of IsAuthenticated is now overwritten by the AllowAny class on the following login function or view only.
def login(request): #a compulsory request parameter as request is always passed by the Url to the view or method. self parameter is not necessary as it is not a method of class.
    email = request.data.get('email') #getting the email data as a JSON through the email field that is input by the front end user and assigning it to email variable. serializer is not required in this case as we are only doing verification of the user and no CRUD operation needs to be done for conversion of JSON to object or vice-versa.
    password = request.data.get('password')
    user = authenticate(username=email,password=password) # checks the given email and password with the registered list of username and password. if the data matches, the same user is returned as an object to the assigned user variable, but if no match occurs, then the variable user gets assigned as 'None'. Returns only one user incase of true as only one user exist for a specific email and pw. every user receives unique token.
    if user == None:
        return Response('Email or password is incorrect!') # case when the data provided by the front-end does not match the data registered in the user table.
    else:
        token,_ = Token.objects.get_or_create(user=user) # get_or_create is a mixed query of Object Relation Manager that returns tuple values(Token and bool). it initially gets the token object from the user field of token table that matches with the logged in user of this function and assigns the token object with the user(left one) key to the token variable of this login function. if user is found on the token table, the token object and "true" bool value is returned to this variable which can be sent as a response but if user is not found, 'false' value is returned instead of error occurence. incase of false, create query runs from get_or_create that makes a user value in the user field and creates the token object. the token object created is then assigned to the token variable. the key value for key field gets auto-created that can be retrieved from object to send the response. "_" variable is assigned for boolean value and "token" variable is assigned for token value.
        return Response(token.key) #sending the key value from key attribute of the retrieved or created token object to the front-end user that can be used to make requests to the API.
            
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
    
    
    