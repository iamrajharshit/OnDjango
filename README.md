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
```
OnDjango\manage.py runserver
```
<img src= "img\03_runserver.png">
- Ignore the error for now.
- Our server has started local `http://127.0.0.1:8000/`

<img src="img\04_server.png">
- Our Django page is running with `DEBUG=True`

