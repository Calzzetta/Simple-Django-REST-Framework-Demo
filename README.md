*Demo Django Application using Django REST Framework*

1. To text create a virtualenv and install the requirements
```
pip install -r requirements.txt
```

2. After that create the SQLite DB using:
```
python manage.py migrate
```

3. Create a demo admin user:
```
python manage.py createsuperuser
```

4. Run the server:
```
python manage.py runserver
```

The admin page will be running on http://localhost:8000/admin/
To see the list of employess, access http://localhost:8000/employee/

To get a specific employee, access http://localhost:8000/employee/<email>/
ex: http://localhost:8000/employee/demo@user.com/