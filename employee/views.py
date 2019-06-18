from django.shortcuts import render
import csv, os

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def addEmployee(request):
    ''' Add an employee to employee_data.csv '''
    if request.method == "POST":
        rawdata = request.POST
        data = {'name':rawdata['name'], 'emp_id':rawdata['emp_id']}

        if not os.path.isfile("employee_data.csv"): isNew = True
        else: isNew = False

        with open("employee_data.csv", "a") as emp_csv:
            writer = csv.DictWriter(emp_csv, fieldnames=['name', 'emp_id'])
            if isNew: writer.writeheader()
            writer.writerow(data)

        return render(request, 'result.html', {'msg':'Employee added succesfully!', 'title':'SUCCESS!'})

    return render(request, 'employee.html')

def displayEmployees(request):
    ''' Display details of all employees from the employee CSV, in a table '''
    if not os.path.isfile('employee_data.csv'):
        return render(request, 'result.html', {'msg':'Employee CSV not found!! Have you added any employees yet?', 'title':'ERROR!'})

    with open("employee_data.csv", 'r') as emp_csv:
        if len(emp_csv.readlines()) <= 2:
            return render(request, 'result.html', {'msg':'Employee CSV is empty!! Have you added any employees yet?', 'title':'ERROR!'})
        emp_csv.seek(0)
        reader = csv.DictReader(emp_csv)
        data = {dict(i)['name']:dict(i)['emp_id'] for i in reader}

    return render(request, 'employee-details-csv.html', {'data':data})

def removeEmployee(request):
    ''' Remove an employee's record from the employee CSV given the name or employee ID '''
    if request.method == "POST":
        postdata = request.POST
        if not os.path.isfile('employee_data.csv'):
            return render(request, 'result.html', {'msg':'Employee CSV not found!! Have you added any employees yet?', 'title':'ERROR!'})

        with open('employee_data.csv', 'r') as emp_csv:
            data = [i for i in list(csv.reader(emp_csv)) if len(i) > 0]

        with open('employee_data.csv', 'w') as emp_csv:
            writer = csv.writer(emp_csv)
            found = False
            for row in data:
                if ('name' in postdata and row[0] == postdata['name']) or ('emp_id' in postdata and row[1] == postdata['emp_id']):
                    found = True
                else: writer.writerow(row)
            return render(request, 'result.html', {'msg':"Specified employee not found!", 'title':'ERROR!'}) if not found else render(request, 'result.html', {'msg':"Employee removed from CSV succesfully!", 'title':'SUCCESS!'})

    return render(request, 'remove-employee.html')
