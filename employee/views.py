from django.shortcuts import render
import csv, os

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def addEmployee(request):
    if request.method == "POST":
        rawdata = request.POST
        data = {'name':rawdata['name'], 'emp_id':rawdata['emp_id']}
        if not os.path.isfile("employee_data.csv"): isNew = True
        else: isNew = False
        with open("employee_data.csv", "a") as emp_csv:
            writer = csv.DictWriter(emp_csv, fieldnames=['name', 'emp_id'])
            if isNew: writer.writeheader()
            writer.writerow(data)
        return render(request, 'employee-added.html')

    return render(request, 'employee.html')

def displayEmployees(request):
    with open("employee_data.csv", 'r') as emp_csv:
        reader = csv.DictReader(emp_csv)
        data = {dict(i)['name']:dict(i)['emp_id'] for i in reader}
    return render(request, 'employee-details.html', {'data':data})

def removeEmployees(request):
    if request.method == "POST":
        if not os.path.isfile('employee_data.csv'): return render(request, 'employee-details.html', {'msg':'Employee CSV not found!!'})
        raw = request.POST
        if 'name' in raw:
            param = 'name'
            val = raw['name']
        else:
            param = 'emp_id'
            val = raw['emp_id']
        with open('employee_data.csv', 'r') as emp_csv:
            data = list(csv.reader(emp_csv))
            emp_csv.seek(0)
            writer = csv.writer(emp_csv)
            found = False
            for row in data:
                if (param == 'name' and data[0] == val) or (param == 'emp_id' and data[1] == val): found = True
                else: writer.writerow(row)
            
