from django.contrib import admin
from .models import User #importing user table from models.py in admin panel to use tokens for authentication.


# Register your models here.

admin.site.register(User) #registering the user table on the admin panel or admin.py
