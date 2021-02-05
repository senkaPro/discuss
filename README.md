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
   
 You can notice i have setup my settings in separate settings module,mainly because i work and store my environment variables in 
 .env file.So this way whatever environment i work im all set up.
 For that reason i use python-dotenv package and i load my env file settings into django, there are two main parts where you need include that package:
 
 _manage.py
```python
#Import python-dotenv package
import dotenv
 
#Load your env file with respect to the directory where you have stored it to the manage.py directory
dotenv.load_dotenv(
    os.path.join(os.path.dirname(), '.env')
 )
 ```
 _wsgi.py or asgi.py
 
```python
#Import python-dotenv package
import dotenv
 
#Load your env file with respect to the directory where you have stored it to the manage.py directory
dotenv.load_dotenv(
    os.path.join(os.path.dirname(), '.env')
 )
 
'''
Firstly it will setup local settings into environment variable for DJANGO_SETTINGS_MODULE,if 
it finds out DJANGO_SETTINGS_MODULE variable in environment variables it will use it
otherwise it will use the default local settings
so in your production environment you will set your DJANGO_SETTINGS_MODULE to your production settings
'''

os.environ.setdefault('DJANGO_SETTINGS_MODULE') = 'config.settings.local'
if os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = os.getenv('DJANGO_SETTINGS_MODULE')
 
```
   
   
   
   
   
   
   
   
   
   
   
   
   
