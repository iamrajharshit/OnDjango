# OnDjango
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
- Ridiculously Fast
- Fully Loaded
- Reassuringly Secure
- Exceedingly Scalable
- Incredibly Versatile

## Creating Venv 
**Venv:** A seprate sandbox to run our program.

### Venv Using uv
Using [uv](https://pypi.org/project/uv/) as it's an extremely fast Python package installer and resolver, written in Rust.
Designed as a drop-in replacement for common `pip` and `pip-tools` workflows.

#### To install uv:
```
pip install uv
```
#### To create venv

```
uv venv  # Create a virtual environment at .venv.

```
#### To activate venv
```
# On Windows.
.venv\Scripts\activate
```
#### To deactivate 
```
deactivate
```
#### To install packages into venv
```
uv pip install -r requirements.txt  # Install from a requirements.txt file.
```
#### Install Django
```
uv pip install Django
```
<img src="img\01_uv pip Django.png">

[Django Doc](https://docs.djangoproject.com/en/5.0/) is in detail explaination.

## Starting Django Project
To start a project in django:
```
django-admin startproject OnDjango
```
- Here, `django-admin` is the main command.
`startproject` is used once, to initate a project.
`OnDjango` is our project name.
- Later will use `startapp` for multiple `apps` in django.

<img src="img\02_Project.png">

We have our OnDjango project ready.
- we have OnDjango a sub-folder inside main OnDjango folder, which is commond in Django projects.

#### Run manage.py
run your `manage.py` using static command `runserver`.
- *Remember the directory, manage.py should be accessible.*
```
OnDjango\manage.py runserver
```
<img src= "img\03_runserver.png">

- Ignore the error for now.
- Our server has started local `http://127.0.0.1:8000/`

<img src="img\04_server.png">

- Our Django page is running with `DEBUG=True`

## Files inside Django project

- **manage.py:** Its a root level.
- **db.sqlite3:** Its a default database in Django.

- **Project folder:** Here it's OnDjango as our project.
    - **setting.py:** One of the main file. Contains config of django project.
    contains details about *Base Dict*, *Secret key*, *Debugging*, *host* etc..
    - **__init__.py:** constructor
    - **urls.py:** routing file
    - **views.py:** routing files -> controller file (business logic)

## Workflow of Django

### Diagram


### Working with views.py
- views.py stores the logical part of the Django project.
- create [views.py](OnDjango\OnDjango\views.py) file inside sub-project folder level.

```
#Giving response 
from django.http import HttpResponse

#response methods
def home(request):
    return HttpResponse("We are working OnDjango")

def Contact(request):
    return HttpResponse("Connect with me at @iamrajharshit")

```
### Next urls handle

Under urls, we first add, `from . import views`. Here (.) refers to the same directory.

Then will add path for home and conctact method.
As `home` is our main page, so it doesnt has any end point *'contact/'* as `views.contact`.
```
from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact')
]
```
#### Run the server:
- *Remember the directory, manage.py should be accessible.*
```
/OnDjango/OnDjango/manage.py runserver
```
#### Home page 
<img src="img\05_home.png">

The localhost `127.0.0.1:8000` returns `HttpResponse("We are working OnDjango")` 

#### Contact page

<img src="img\06_contact.png">

Add contact at the end of the localhost `127.0.0.1:8000`
- `127.0.0.1:8000/contact`returns `HttpResponse("Connect with me at @iamrajharshit")`


### Using Templates

**Templates:** They are a crucial part of the Model-View-Template (MVT) design pattern used for building web applications. 
- They contains `html` files.
- They provide a way to separate the presentation layer (what the user sees) from the business logic (how the application works).
- Where to make templates depends on, how are we seeing the files and whats our `settings.py`

**Static:** It contains static files refer to assets that are used by your web application but don't change dynamically based on user input or database data. 
- Static files like imgs, fonts, `css` and `js` files.

 Here, will add *templates* and *static* folder under *root* folder.

- Under *templates* will add a html file `index.html`
-  Now will load and return this template.

### Under views.py
As we have to render our *template*, will import `render` from django.shortcuts.
- Will try to access `index.html` using render on our home page.
```
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("We are working OnDjango")
    return render(request,'index.html') #using render

def contact(request):
    return HttpResponse("Connect with me at @iamrajharshit")

```

### Error: TemplateDoesNotExist at /

<img src="img\07_error.png">

- Will have to mention from where to load our *templates* under `setting.py` file.

Under **TEMPLATES** section will mention under which ***DIRS*** ***templates*** are present for use.
```
'DIRS':['templates'],
```
If still Error exsits like : `Error: TemplateDoesNotExist at/`
Then `import os` and try this code, specifying the path:
```
'DIRS': [os.path.join(BASE_DIR,'templates')],
```
Output:
<img src="img\08_fixed error.png">