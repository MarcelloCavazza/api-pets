
# Instalation
* First set the enviroment:(linux/mac)

Bash:
```
  python3 -m venv .venv # create basic system files
  source .venv/bin/activate.fish  #to enter in fish's terminal
```

* Django instalation:

Fish bash:
```
  pip install Django
  pip install django-rest-framework
```
    
* Django setting project:

Fish bash:
```
  django-admin startproject api_pets .
```
* Django executing server:

Fish bash:
```
  python manage.py runserver
```
* Django setting migrations that create models that will go to the database:

Fish bash:
```
  python manage.py makemigrations
```
* Django applying all the setted migrations to the database:

Fish bash:
```
  python manage.py makemigrations
```
