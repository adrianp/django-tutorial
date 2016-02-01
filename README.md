# django-tutorial
My run at the django tutorial

# Setup

```
$ mkvirtualenv django-tutorial
$ workon django-tutorial
$ cdvirtualenv
$ mkdir src
$ cd src
$ git clone https://github.com/adrianp/django-tutorial.git
$ cd django-tutorial
$ cd django-polls
$ python setup.py sdist
$ cd ..
$ pip install -r requirements.txt
$ python manage.py makemigrations polls
$ python manage.py migrate
$ python manage.py createsuperuser
```

# Run

## Server

```
$ python manage.py runserver
```

## Shell
```
$ python manage.py shell_plus
```

## Tests
```
$ python manage.py test polls
```
