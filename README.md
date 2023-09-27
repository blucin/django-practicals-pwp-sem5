# Python and Web Programming Practicals

<!-- metadata (use pandoc) 
% title: Python and Web Programming Practical 9
% author: Akshar Patel (12102110501003) CSE-IoT Batch As
% date: September 28, 2023
-->

## Installation 
1. Create a virtual environment
```bash
python -m venv env
.\env\Scripts\Activate.ps1
```

2. Install from requirements.txt
```bash
pip install -r requirements.txt
```

## Practical 9.1

## 1. Introduction to MVC Framework:

MVC (Model-View-Controller) is a design pattern commonly used in web development to separate an application into three interconnected components to enhance modularity and maintainability. Here's a brief
overview of each component:
1. Model: The model represents the application's data and business logic. It interacts with the database to retrieve, store, and manipulate data. It is responsible for data storage, retrieval, and manipulation.
2. View: The view is responsible for presenting the data to the user. It handles the presentation layer and rendering of content. It doesn't contain business logic but rather displays data provided by the model.
3. Controller: The controller acts as an intermediary between the model and view. It receives user input from the view, processes it, and interacts with the model to retrieve or update data. The controller also updates the view to reflect changes in the model.

## 2. Django Installation and Server Configuration:

### 2.1. Creating a virtual environment

```bash
python -m venv env   
.\env\Scripts\Activate.ps1
```

### 2.2. Creating a project

```bash
mkdir apps
pip install Django
python manage.py migrate
python manage.py runserver
```

### 2.3. Creating an app inside a folder

```bash
mkdir apps/prac9_1
django-admin startapp prac9_1 apps/prac9_1
```

- Now our project structure looks like this:

```bash
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        28-09-2023  12:35 AM                apps
d-----        28-09-2023  12:26 AM                env
d-----        28-09-2023  12:31 AM                project
-a----        28-09-2023  12:31 AM         131072 db.sqlite3
-a----        28-09-2023  12:30 AM            685 manage.py
-a----        28-09-2023  12:45 AM           2235 README.md
```


### 2.4. Adding the app to the project

- Our app is located in apps/prac9_1
- We need to add it to the INSTALLED_APPS list in settings.py in the project folder

```python
import sys
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Add apps directory to Python paths
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

... 

INSTALLED_APPS = [
    'prac9_1',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]
```

### 2.5. Creating a model in prac9_1/models.py

```python
from django.db import models

# test model for prac9_1
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
```

### 2.6. Registering the model in prac9_1/admin.py

```python
from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.register(Product)
```

### 2.7. Creating a view in prac9_1/views.py

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the prac9_1 index.")
```

### 2.8. Creating a URL in prac9_1/urls.py

```bash
touch apps/prac9_1/urls.py
```

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### 2.9. Adding the URL to the project's URL file

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('prac9_1/', include('apps.prac9_1.urls')),
    path('admin/', admin.site.urls),
]
```

### 2.10. Running the server

```bash
python manage.py runserver
```

- Now go to `http://127.0.0.1:8000/prac9_1/` and you should see the message

![index page demo](assets/prac9_1_index.png)

<!-- END OF PRAC9_1 -->

## Practical 9.2

### Template Tags, Variables, Loops, Control Structure, etc

- Django templates are a powerful tool for generating dynamic HTML and other text-based formats. They allow you to embed Python-like code directly within your HTML, making it easy to display dynamic content and control the rendering of your web pages. Here's an overview of some of the key features of Django templates:

1. Template:

- Template tags are enclosed in `{% ... %}` and are used to perform actions, control logic, or insert content dynamically into the template.
- Examples:

- If statements

```html
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Welcome, new user!</p>
{% endif %}
```

- For loops

```html
{% for product in products %}
    <p>{{ product.name }}: {{ product.price }}</p>
{% endfor %}
```

- Template Block

```html
{% block content %}
    <p>This is the content of the page.</p>
{% endblock %}
```

2. Variables:

- Variables are enclosed in `{{ ... }}` and are used to display dynamic content in the template.

```html
<p>{{ product.name }}: {{ product.price }}</p>
```

3. Filters:

- Filters are used to modify the output of a variable. They are appended to the variable name and are separated by a pipe character (`|`).

```html
<p>{{ product.name|upper }}: {{ product.price }}</p>
```

4. Loops:

- Loops are used to iterate over a list of items and perform an action for each item in the list.

```html
{% for product in products %}
    <p>{{ product.name }}: {{ product.price }}</p>
{% endfor %}
```

5. Control Structure:

- Control structures are used to control the flow of the template. They are enclosed in `{% ... %}` and include if statements, for loops, and other logic.

```html
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Welcome, new user!</p>
{% endif %}
```

6. Inheritance:

- Inheritance allows you to create a base template that can be extended by other templates. It is used to avoid code duplication and to create a consistent look and feel across multiple pages.

`base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <div id="content">
        {% block content %}
        {% endblock %}
    </div>
</body>s
```

`usage.html`

```html
{% extends "base.html" %}

{% block title %}Usage{% endblock %}

{% block content %}
    <p>This is the usage page.</p>
{% endblock %}
```

7. Template Inheritance:

- You can include other templates within a template using the `{% include "template_name" %}` tag.

8. Comments:

- Comments are enclosed in `{# ... #}` and are used to add comments to the template.

```html
{# This is a comment #}
```

9. Template Context:

- Context data, typically provided by the view, is used to populate variables in the template.

`views.py`

```python
def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'index.html', context)
```

`index.html`

```html
{% for product in products %}
    <p>{{ product.name }}: {{ product.price }}</p>
{% endfor %}
```

- Django's template language is flexible and allows you to build complex web pages while keeping the presentation logic separate from the business logic in your views It's an essential part of Django's "Don't Repeat Yourself" (DRY) philosophy, enabling efficient and maintainable web development.


### 9.1. Creating prac9_2 app

```bash
mkdir apps/prac9_2
django-admin startapp prac9_2 apps/prac9_2
```

### 9.2. Adding the app to the project

```python
INSTALLED_APPS = [
    'prac9_1',
    'prac9_2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]
```

### 9.3. Creating a template base.html

- We will create a base template that will be extended by other templates.

```bash
mkdir apps/prac9_2/templates
touch apps/prac9_2/templates/base.html
```

- Now we will add the following code to the base.html file

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>
        {% block title %} 
            Placeholer Title 
        {% endblock %}
    </title>
</head>
<body>
    <div id="content">
        {% block content %}

        {% endblock %}
    </div>
</body>
</html>
```

- Now we will create a template called `index.html` that will extend the base template

```bash
touch apps/prac9_2/templates/index.html
```

- Now we will add the following code to the index.html file

```html
{% extends "base.html" %}

{% block title %} 
    Index Page 
{% endblock %}

{% block content %}
    <h1>Index Page</h1>
{% endblock %}
```

### 9.4. Creating a view in prac9_2/views.py

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
```

### 9.5. Creating a URL in prac9_2/urls.py

- We will create a URL file for the prac9_2 app

```bash
touch apps/prac9_2/urls.py
```
- Now we will add the following code to the `urls.py` file

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### 9.6. Adding the URL to the project's URL file

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('prac9_1/', include('apps.prac9_1.urls')),
    path('prac9_2/', include('apps.prac9_2.urls')),
    path('admin/', admin.site.urls),
]
```

### 9.7. Running the server

```bash
python manage.py runserver
```

- Go to `http://127.0.0.1:8000/prac9_2/` and you should see the message 

![index page demo](assets/prac9_2_index.png)


### 9.8 Creating a template for demonstrating variables, loops, control structures, etc

- We will create a template called `demo.html` that will extend the base template

```bash
touch apps/prac9_2/templates/demo.html
```

- Add the following content to `demo.html`

```html
{% extends "base.html" %}

{% block title %} 
    Demo Page 
{% endblock %}

{% block content %}
    <h1>Demo Page</h1>
    <p>Variable: {{ variable }}</p>
    <p>Filter: {{ variable|upper }}</p>
    <p>Loop:</p>
    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
    <p>Control Structure:</p>
    {% if user.is_authenticated %}
        <p>Welcome, {{ user.username }}!</p>
    {% else %}
        <p>Welcome, new user!</p>
    {% endif %}
{% endblock %}
```

- Now we will add a view to `prac9_2/views.py`

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def demo(request):
    context = {
        'variable': 'This is a variable',
        'items': ['Item 1', 'Item 2', 'Item 3']
    }
    return render(request, 'demo.html', context)
```

- Now we will add a URL to `prac9_2/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo/', views.demo, name='demo'),
]
```

- Run the server and go to `http://127.0.0.1:8000/prac9_2/demo/` and you should see the output.

![template demo screenshot](assets/prac9_2_demo.png)

<!-- END OF PRAC9_2 -->

## Practical 9.3

### 9.1. Creating prac9_3 app

```bash
mkdir apps/prac9_3
django-admin startapp prac9_3 apps/prac9_3
```

### 9.2. Adding the app to the project

```python
INSTALLED_APPS = [
    'prac9_1',
    'prac9_2',
    'prac9_3',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]
```

### 9.3. Create a model for the form

- We will create a model called `FormData` that will store the username and email of the user. Go to `prac9_3/models.py` and add the following code

```python
from django.db import models

# Create your models here.
class FormData(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username
```

### 9.4. Registering the model in prac9_3/admin.py

```python
from django.contrib import admin
from .models import FormData

# Register your models here.
admin.site.register(FormData)
```

### 9.5. Make and run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 9.6. Creating a template base.html from prac9_2

```bash
mkdir apps/prac9_3/templates
cp apps/prac9_2/templates/base.html apps/prac9_3/templates/base.html
```

### 9.7. Creating a form html file

```bash
touch apps/prac9_3/templates/form.html
```

- Now we will add the following code to the `form.html` file to ask the user for username and email. On submit it will redirect us to a page `formData.html` to show the filled out form.

`form.html`

```html
{% extends "base.html" %}

{% block title %} 
    Form Page 
{% endblock %}

{% block content %}
    <h1>Form Page</h1>
    <form action="{% url 'formData' %}" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <label for="username">Username:</label>
        <input type="text" name="username" id="username">
        <label for="email">Email:</label>
        <input type="email" name="email" id="email">
        <input type="submit" value="Submit">
    </form>
{% endblock %}
```

`formData.html`

```html
{% extends "base.html" %}

{% block title %} 
    Form Data Page 
{% endblock %}

{% block content %}
    <h1>Form Data Page</h1>
    <table>
        <thead>
            <tr>
                <th>Username</th>
                <th>Email</th>
            </tr>
        </thead>
        <tbody>
            {% for data in formdata %}
                <tr>
                    <td>{{ data.username }}</td>
                    <td>{{ data.email }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
```

### 9.5. Create a `form.py` file

```bash
touch apps/prac9_3/form.py
```

- Now we will add the following code to the `form.py` file to create a form

```python
from django import forms

class FormDataForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
```

### 9.6. Creating a view in prac9_3/views.py

```python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .form import FormDataForm
from .models import FormData

# Create your views here.
def index(request):
    return render(request, 'index.html')

def form(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/prac9_3/formData/')
    else:
        form = FormDataForm()
    return render(request, 'form.html', {'form': form})

def formData(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            FormData.objects.create(username=username, email=email)
            return HttpResponseRedirect('/prac9_3/formData/')
    else:
        form = FormDataForm()
    return render(request, 'formData.html', {'formdata': FormData.objects.all()})
```

### 9.7. Creating a URL in prac9_3/urls.py

- We will create a URL file for the prac9_3 app

```bash
touch apps/prac9_3/urls.py
```

- Now we will add the following code to the `urls.py` file

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('formData/', views.formData, name='formData'),
]
```

### 9.8. Adding the URL to the project's URL file

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('prac9_1/', include('apps.prac9_1.urls')),
    path('prac9_2/', include('apps.prac9_2.urls')),
    path('prac9_3/', include('apps.prac9_3.urls')),
    path('admin/', admin.site.urls),
]
```

### 9.9. Running the server

```bash
python manage.py runserver
```

- Go to `http://127.0.0.1:8000/prac9_3/form/` and fill out the form

[form](assets/prac9_3_form.png)

- After submitting the form you should see the output

[form data](assets/prac9_3_form_redirect.png)

<!-- END OF PRAC9_3 -->

## Practical 9.4

### 9.1. Creating prac9_4 app

```bash
mkdir apps/prac9_4
django-admin startapp prac9_4 apps/prac9_4
```

### 9.2. Adding the app to the project

```python
INSTALLED_APPS = [
    'prac9_1',
    'prac9_2',
    'prac9_3',
    'prac9_4',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]
```

### 9.3. Creating a template base.html from prac9_2

```bash
mkdir apps/prac9_4/templates
cp apps/prac9_2/templates/base.html apps/prac9_4/templates/base.html
```

### 9.4. Creating a model for file upload

- We will create a model called `FileUpload` that will store the file name and the file itself. Go to `prac9_4/models.py` and add the following code

```python
from django.db import models

# Create your models here.
class FileUpload(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name
```