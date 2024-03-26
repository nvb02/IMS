from django.urls import path #importing path function from main urls.py to make urls here.
from .views import * #importing the views from view.py to make url for the views to be called.

urlpatterns = [
    path('department/',DepartmentView.as_view({'get':'list','post':'create'})), #as_view method is defined since it is a view that inherits modelviewset (API view). as_view states that if 'get' request is recieved, the 'list' method that exists in modelviewset is run that returns every data of the department model, whereas when the request called is 'post', the data is created in the model through 'create' method. the logics of CRUD operations defined in modelviewset methods does not match with the names of request method which is why we have to manually define what to run when get or post request is received. only the defined requests can be returned in the url, ex- put request provided with this url will return an error. but the front-end can request any kind of method whether or not the method lies in this url, so handling the request should be considered properly. here, modelviewset automatically shows error if a non-defined method is requested.
    path('department/<int:pk>/',DepartmentView.as_view({'get':'retrieve','put':'update','delete':'destroy'})), #in this url, specific data is returned through the ID provided in the url when 'get' request is received with the help of 'retrieve' method. this is another nature of the get request where ID is sent from front end to request a specific data. If 'put' request is received with an ID, 'update' method is run from modelviewset to change or alter the specific data. And when 'delete' request is passed from front-end regarding a specific data, 'destroy' method is called to delete that specific data with the help of ID from the model.
    # this is the way to define URLS in CLASS BASED API VIEWS (MODEL VIEW SET) compared to that of NORMAL VIEWS.   
    path('resource/',ResourceView.as_view()),
    path('resource/<int:pk>/',ResourceDetailView.as_view()),
    path('employeeprofile/',EmployeeProfileView.as_view({'get':'list','post':'create'})),
    path('employeeprofile/<int:pk>/',EmployeeProfileView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('vendor/',VendorView.as_view({'get':'list','post':'create'})),
    path('vendor/<int:pk>/',VendorView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('purchase/',PurchaseView.as_view({'get':'list','post':'create'})),
    path('purchase/<int:pk>/',PurchaseView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
]
