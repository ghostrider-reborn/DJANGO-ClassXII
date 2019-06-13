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

#def removeEmployees(request):
#    if not os.path.isfile('employee_data.csv', 
