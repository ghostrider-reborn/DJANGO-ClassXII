from django.shortcuts import render, redirect
from employee_v2.models import employee

# Create your views here.
isLoggedIn = False

def home(request):
    return render(request, 'home.html')

def login(request):
    users = {'hackerman':'h4ck3rm4nn', 'adithya':'urmomgay', 'admin':'godoftheinternet'}
    global isLoggedIn
    if isLoggedIn: return redirect('/adminpage')
    if request.method == "POST":
        data = request.POST
        login_id, password = data['login_id'], data['password']
        if login_id in users:
            if password == users[login_id]:
                isLoggedIn = True
                return redirect('/adminpage')
        return render(request, 'result.html', {'msg':'Incorrect username and/or password you fool!'})
    return render(request, 'login.html')

def adminPage(request):
    global isLoggedIn
    if not isLoggedIn: return render(request, 'result.html', {'msg':'Login required to access this page!', 'title':'ERROR!'})
    return render(request, 'admin.html')

def addEmployee(request):
    global isLoggedIn
    if not isLoggedIn: return render(request, 'result.html', {'msg':'Login required to access this page!', 'title':'ERROR!'})
    if request.method == "POST":
        data = request.POST
        name = data['name']
        emp_id = data['emp_id']
        new_emp = employee(name=name, emp_id=emp_id)
        new_emp.save()
        return render(request, 'result.html', {'msg':'Employee added succesfully!', 'title':'SUCCESS!''})
    return render(request, 'employee.html')

def displayEmployees(request):
    global isLoggedIn
    if not isLoggedIn: return render(request, 'result.html', {'msg':'Login required to access this page!', 'title':'ERROR!})
    employees = employee.objects.all()
    return render(request, 'employee-details.html', {'employees':employees})

def logout(request):
    global isLoggedIn
    if isLoggedIn:
        isLoggedIn = False
        return render(request, 'result.html', {'msg':'Logged out succesfully!'})
    return render(request, 'result.html', {'msg':'You\'re not even logged in you fool!', 'title':'ERROR!'})

''' # WIP
    def removeEmployee(request):
    global isLoggedIn
    if not isLoggedIn: return render(request, 'result.html', {'msg':'Login required to access this page!'})
    if request.method == "POST":
        data = request.post
        try:
            if 'name' in data: emp = employee.objects.get(name = data['name'])
            elif 'emp_id' in data:emp = employee.objects.get(emp_id = data['emp_id'])
            emp.delete()
        except employee.DoesNotExist: render(request, 'result.html', {'msg':"Specified employee not found!", 'title':'ERROR!'}) '''
