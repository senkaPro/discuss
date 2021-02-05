# Django-API-Project-Template

<p>This is a django start project template with custom project structure.
When creating django-admin startproject ExampleProject, django structure its layout in a way not suitable for me 
and bit confusing if you are new to django app development.For example django will create nested project folder 
with same name as your project name which looks a bit ugly for my preferrences.</p>

```python
EampleProject
   \
   |_ExampleProject
   |   |_ __init__.py
   |   |_ urls.py
   |   |_ settings.py
   |   |_ wsgi.py
   |   |_ asgi.py
   |_manage.py
 ```
 So the idea of this django template is to give more meaningful way of organising my project directories,
 i preffer working on something like this:
  ```python
 ExampleProject
   \
   |_config
   |   |_ __init__.py
   |   |_ urls.py
   |   |_ settings
   |   |  |_ __init__.py
   |   |  |_ local.py
   |   |  |_ development.py
   |   |  |_ production.py
   |   |  
   |   |_ wsgi.py
   |   |_ asgi.py
   |_ manage.py   
   |
   |_ apps
   |   |_first_app_package
   |   |_second_app_package
   |   |  |_ __init__.py
   |   |  |_ models.py
   |   |  |_ urls.py
   |   |  |_ views.py
   |   |  |_ serializers.py
   |   |  |_ admin.py
   |   |  |_ tests.py
   |   |  |_ apps.py
   |   |
   |   |_ utils_app_package
   |      |_ __init__.py
   |  
   |_ .env
   |_ .gitignore
   |_ Pipfile
   |_ Pipfile.lock
   |_ Procfile
 ```
 This pattern is more suitable and whatever environment you are working its easy to setup fast and have instant returned results.
 Usually when you working from local environment you want to have debug=True and in production settings you wanna have tottaly different setups, so it 
 easy to setup with your team and all have same working environments.
 Having separate apps directory make it easier for navigating through the project and for later scaling and deploying.
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
