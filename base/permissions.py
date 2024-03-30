from rest_framework.permissions import DjangoModelPermissions #this class allows user to only request to API according to his or her allowed permissions.

class CustomModelPermission(DjangoModelPermissions): #inorder to overwrite the logic of get request so that only allowed or permitted user can request to view.
    perms_map = { #overwriting the perms_map attribute to make changes to the Get request
        'GET': ['%(app_label)s.view_%(model_name)s'], #creating permission check for get request to compare with the user data whether it has the view permission or not.
        'OPTIONS': [],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
