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
        name, emp_id = data['name'], data['emp_id']
        if any(int(emp_id) == emp.emp_id for emp in employee.objects.all()):
            return render(request, 'result.html', {'msg':'Employee ID already exists!', 'title':'ERROR!'})
        new_emp = employee(name=name, emp_id=emp_id)
        new_emp.save()
        return render(request, 'result.html', {'msg':'Employee added succesfully!', 'title':'SUCCESS!'})
    return render(request, 'employee.html')

def displayEmployees(request):
    global isLoggedIn
    if not isLoggedIn: return render(request, 'result.html', {'msg':'Login required to access this page!', 'title':'ERROR!'})
    employees = employee.objects.all()
    return render(request, 'employee-details.html', {'employees':employees})

def logout(request):
    global isLoggedIn
    if isLoggedIn:
        isLoggedIn = False
        return render(request, 'result.html', {'msg':'Logged out succesfully!', 'title':'SUCCESS!'})
    return render(request, 'result.html', {'msg':'You\'re not even logged in you fool!', 'title':'ERROR!'})

def removeEmployee(request):
    global isLoggedIn
    if not isLoggedIn: return render(request, 'result.html', {'msg':'Login required to access this page!', 'title':'ERROR!'})
    if request.method == "POST":
        emp_id = int(request.POST['emp_id'])
        try:
            employee.objects.get(emp_id = emp_id).delete()
            return render(request, 'result.html', {'msg':'Employee removed successfully!', 'title':'SUCCESS!'})
        except employee.DoesNotExist: return render(request, 'result.html', {'msg':"Specified employee not found!", 'title':'ERROR!'})
    return render(request, 'remove-employee.html')

'''def searchEmployee(request):
    global isLoggedIn
    if not isLoggedIn: return render(request, 'result.html', {'msg':'Login required to access this page!', 'title':'ERROR!'})
    if request.method == "POST":
        data = request.POST
        if 'name' in data:
            names = []
            for emp in employee.objects.all():
                if any(data['name'].lower() == i.lower() for i in str(emp.name).split()): names.append(emp.name)
            if names == []: return render(request, 'result.html', {'msg':"No search results!", 'title':'ERROR!'})
            else: emp_ids = employee.objects.all().filter(name=emp.name).emp_id
            return render(request, 'search-results.html', {'names':names, 'emp_ids':emp_ids})
        else:
            try:
                names = (employee.objects.get(emp_id = emp_id), )
                emp_ids = (emp)'''
