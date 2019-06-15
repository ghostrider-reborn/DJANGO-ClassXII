# DJANGO-ClassXII
My 12th grade computer science Django practice project, named "hackermann".
____
Currently consists of a homepage and W.I.P app named 'employee' with the following features:
* Add an employee (employee name and employee ID), which gets saved to a CSV
* List all employees by their names and IDs in a table

TODO:
* Implement removal of an employee by their name or ID
* Implement searching an employee by their name or ID
* Move to SQLite DBs rather than stupid CSVs
* Add more employee data like date of joining, salary, mobile number etc

How to launch the server?
----
* Assuming you have python3 and pip installed, install virtual env: `pip install virtualenv`
* Make a new folder which will contain the project stuff. Open CMD/terminal there and run `virtualenv venv` 
* Inside that folder clone this repository to a subfolder namely 'hackermann': `git clone https://github.com/ghostrider-reborn/DJANGO-ClassXII hackermann`
* Activate virtualenv by running `venv\scripts\activate` OR in case of Linux: `source venv/scripts/activate`
* Navigate your shell into the 'hackermann' subfolder and run: `python manage.py runserver` OR in case of linux: `python3 manage.py runserver`
* You can find your server up and running at `localhost:8000`
