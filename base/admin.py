from django.contrib import admin
from .models import User #importing user table from models.py in admin panel to use tokens for authentication.


# Register your models here.

@admin.register(User) #registering the user table on the admin panel or admin.py
class UserAdmin(admin.ModelAdmin):
    search_fields = User.SearchableFields #creating search field variable to search needed to be performed for token purpose.

