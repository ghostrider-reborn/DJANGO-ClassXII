"""hackermann URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from employee import views as views_csv
from employee_v2 import views

''' CSV-based employee app (deprecated)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_csv.homepage, name='home'),
    path('addemployee/', views_csv.addEmployee, name='addemployee'),
    path('remove-employee/', views_csv.removeEmployee, name='remove-employee'),
    path('employee-details-csv/', views_csv.displayEmployees, name='employee-details-csv'), '''

# SQLite-based employee app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('adminpage/', views.adminPage, name='adminpage'),
    path('add-employee/', views.addEmployee, name='add-employee'),
    path('employee-details/', views.displayEmployees, name='employee-details'),
    path('employee-details-csv/', views_csv.displayEmployees, name='employee-details-csv'),
    path('remove-employee/', views.removeEmployee, name='remove-employee'),
]
