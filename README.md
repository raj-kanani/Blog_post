### If you wish to run your own build, first ensure you have python globally installed in your computer

### After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

```
$ pip install virtualenv
```
## Dependencies :
 
### cd into your the cloned repo as such:
```
$ cd blog_backend
```

### Create and fire up your virtual environment:

```
$ virtualenv venv 
```
```
$ source venv/bin/activate
```
### Install the dependencies needed to run the app:

```
$ pip install -r requirements.txt
```

### Migration command

```
$ python manage.py makemigrations
$ python manage.py migrate

The perform migrations on each service individually.
The order is mentioned below:
	>>> BlogPost
	>>> Comment      
```

### Create super admin user

```
$  python manage.py createsuperuser
	>>>  Username : Admin@123
	>>>  Email address : admin@gmail.com
	>>>  Password : Admin@123
```

### Run django server

```
$ python3 manage.py runserver
```

### You can now access the api service on your browser by using

[    http://localhost:8000/app/
](    http://localhost:8000/app/
)
# Blog_post
# blog_backend
# blog_backend
