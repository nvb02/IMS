from django.db import models
from django.contrib.auth.models import AbstractUser #to make a custom user table to create certain changes. in the models class of auth, the users are defined. in abstractuser, the logics of users are hidden but are usable to create a custom user table.

# Create your models here.

class User(AbstractUser): #making custom user table, every important aspects of user sessions,login,logout are stored in AbstractUser class which is crucial that is inherited here.
    email = models.EmailField(unique=True) #email is a unique identifier to define the user that should be unique for every different user. unique=true ensures that the same value is not used multiple times in the same field.
    password = models.CharField(max_length=300) #passwords get encrypted and increases in size and stored in db that is why the length of password should be huge.
    username = models.CharField(max_length=300,default='username') # changing or overwriting the user table already defined. in django's user table, the username field is defined as unique stating that username and password is a must to login. the default value here states that if left empty, the phrase username will be stored without any null value.

    USERNAME_FIELD = 'email' #the functionality of this object is that the main fields changes from username:password to email:password.
    REQUIRED_FIELDS = ['username'] #required field is stated for username as it gets neglected when main fields become email and password, django also states that username field should be provided and is highly needed.
    
    #the user table should always be created at the first because making it later returns errors.
    

class Department(models.Model):
    name = models.CharField(max_length=300)
    
class Resource(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    stock = models.IntegerField()
    department = models.ManyToManyField(Department) #this field is used in case of many to many relationship
    price = models.FloatField()
    
class EmployeeProfile(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    number = models.IntegerField()
    email = models.EmailField() #this field only stores emails.
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True) #the foreign key is used incase of one to many relationship, the table to which this object is related to should also be defined, on_delete keyword argument is passed because incase a data is deleted on the linked table or class(Department), then either "SET_NULL" or "CASCADE" method can be used. CASCADE deletes the data of this table if the data related on the linked table gets deleted. this method is helpful if the db needs to clean the storage. SET_NULL ensures if any data in department table gets deleted, the related datas of that table or class such as here in employeeprofile, the value gets changed to null. to do this, this field should be nullable which is why "null should be == True". on contrary, by default every field is required (Required Field) to be filled but by putting null=true, the field can be left empty.
    
class Vendor(models.Model):
    name = models.CharField(max_length=300)
    number = models.IntegerField()
    email = models.EmailField()
    
class Purchase(models.Model):
    resource = models.ForeignKey(Resource,on_delete=models.CASCADE) #if the resource data gets deleted in the resource table, the purchase data will be deleted along with it.
    purchase_quantity = models.IntegerField()
    purchase_price = models.FloatField()
    purchased_from = models.ForeignKey(Vendor,on_delete=models.CASCADE) #if the vendor data gets deleted on vendor table, the purchase data related to vendor should also get deleted. Note that if the class or table being called to fetch the foreign key is made after this class for instance, Vendor class in this case, then it will show error. the table being referred to for foreign key should be above the calling class, but if it is below this class, the class can be called by inserting the class name inside the quotation 'Vendor', this will find the class wherever it lies in models.py not necessarily by staying above the calling class.
    