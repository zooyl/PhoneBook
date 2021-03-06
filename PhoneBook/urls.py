"""PhoneBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
import Book.views

urlpatterns = [
    path('', Book.views.home, name='home'),
    path('admin/', admin.site.urls),
    path('new/', Book.views.NewBasic.as_view()),
    path('edit/<int:pk>', Book.views.EditBasic.as_view()),
    path('details/full/<int:id>', Book.views.full_details),
    path('details/basic/<int:id>', Book.views.basic_details),
    path('delete/<int:pk>', Book.views.PersonDelete.as_view()),
    path('delete/address/<int:pk>', Book.views.AddressDelete.as_view()),
    path('delete/phone/<int:pk>', Book.views.PhoneDelete.as_view()),
    path('delete/email/<int:pk>', Book.views.EmailDelete.as_view()),
    path('delete/group/<int:pk>', Book.views.GroupDelete.as_view()),
    path('new/group', Book.views.CreateGroup.as_view()),
    path('group/list', Book.views.group_list),
    path('add/address/<int:id>', Book.views.AddAddress.as_view()),
    path('add/phone/<int:id>', Book.views.AddPhone.as_view()),
    path('add/email/<int:id>', Book.views.AddEmail.as_view()),
    path('add/group/<int:id>', Book.views.AddGroup.as_view()),
    path('search/', Book.views.SearchUser.as_view()),
]
