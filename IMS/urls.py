"""
URL configuration for IMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #importing include function from django.urls to include urls from other sources or app folders (in this case, base app).

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')) #if there is nothing requested after IP Address in the url, then it is defined that the base urls can be requested.
]
