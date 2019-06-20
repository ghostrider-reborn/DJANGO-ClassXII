# DJANGO-ClassXII
My 12th grade computer science Django practice project, named "hackermann".
____
Currently consists of an app named 'employee' with a homepage, and an admin page which gives access to the following features:
* Add an employee (employee name and employee ID), which gets saved to the `employee-data.sqlite3` database
* List all employees by their names and IDs in a table
* Remove an employee by their employee ID
* Search for an employee by their name or ID

The admin page can be accessed by logging in using the usernames & passwords which are stored as a dictionary in `views.py` of the employee_v2 app.

This project also consists of a deprecated app 'employee' (v1) which uses CSV to store employee data.

TODO:
* Implement changing name or ID of an existing employee
* Add more employee data like date of joining, salary, mobile number etc

How to launch the server?
----
* Assuming you have python3 and pip installed, install virtual env: `pip install virtualenv`
* Make a new folder which will contain the project stuff. Open CMD/terminal there and run `virtualenv venv`
* Inside that folder clone this repository to a subfolder namely 'hackermann': `git clone https://github.com/ghostrider-reborn/DJANGO-ClassXII hackermann`
* Activate virtualenv by running `venv\scripts\activate` OR in case of Linux: `source venv/scripts/activate`
* Install django inside this virtualenv: `pip install django`
* Navigate your shell into the 'hackermann' subfolder and run: `python manage.py runserver` OR in case of linux: `python3 manage.py runserver`
* You can find your server up and running at `localhost:8000`
