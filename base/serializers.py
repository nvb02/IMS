from rest_framework import serializers #serializers module from rest_framework allows conversion of object data into json
from .models import * #importing everything from models.py to serializers.py
from django.contrib.auth.models import Group #to convert objects from group table into json format while querying.

class GroupSerializer(serializers.ModelSerializer): #using this serializer only for listing purpose, Creation or deletion or changing of groups is done through the database.
    class Meta:
        model = Group
        fields = ['id','name'] #id field is the value used by the user during registration, and name field is the value of the group name.
        
class UserSerializer(serializers.ModelSerializer): #to convert the user registration from front-end JSON into an object to be stored in the db.
    class Meta:
        model = User
        fields = ['email','password','groups'] #all the fields are not required to be converted into object as many of them are abstract and not needed, only required fields should be mentioned. additional fields such as user photo, user no, user address, user contact etc can be inserted as per the requirements.

class DepartmentSerializer(serializers.ModelSerializer): #we need to create a single class for a single model (creating a department serializer to convert object of department model into json ), inheriting ModelSerializer from serializers that consist of logics to convert objects into json. in functions, we cannot inherit classes so class-based serializers must be made instead of function-based serializers. ModelSerializer also converts the json file coming from front-end into object to be usable in back-end from python.
    class Meta: #meta class defines extra behavior of a serializer class that can also be used at models to define extra or additional behaviors or natures.
        model = Department #model object states that pbjects of department model will get serialized.
        fields = '__all__' #fields states the objects that needs to get converted into json or json files that will get converted into objects, ex==> ['name','ID'],  '__all__' converts every field of department model into json.
        
class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__' 
        
class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = '__all__'
        
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'