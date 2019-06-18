from django.shortcuts import render, redirect
from employee_v2.models import employee

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    users = {'hackerman':'h4ck3rm4nn', 'adithya':'urmomgay', 'admin':'godoftheinternet'}
    if request.method == "POST":
        data = request.POST
        login_id = data['login_id']
        password = data['password']
        if login_id in users:
            if password == users[login_id]: return redirect('/adminpage')
        return render(request, 'result.html', {'msg':'Incorrect username and/or password you dumbass!'})
    return render(request, 'login.html')

def adminPage(request):
    return render(request, 'admin.html')

def addEmployee(request):
    if request.method == "POST":
        data = request.POST
        name = data['name']
        emp_id = data['emp_id']
        new_emp = employee(name=name, emp_id=emp_id)
        new_emp.save()
        return render(request, 'result.html', {'msg':'Employee added succesfully!'})
    return render(request, 'employee.html')

def displayEmployees(request):
    employees = employee.objects.all()
    return render(request, 'employee-details.html', {'employees':employees})
