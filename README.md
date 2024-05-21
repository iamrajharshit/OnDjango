# OnDjango
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
- Ridiculously Fast
- Fully Loaded
- Reassuringly Secure
- Exceedingly Scalable
- Incredibly Versatile
### Creating Venv in python using uv
**Venv:** A seprate sandbox to run our program.
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