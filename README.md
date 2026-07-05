Iniciar Projeto

```
python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py startapp APPNAME
```

Migrar base de dados

```
python manage.py makemigrations
python manage.py migrate
```

Criar SU

```
python manage.py createssuperuser
python manage.py changepassword USERNAME
```