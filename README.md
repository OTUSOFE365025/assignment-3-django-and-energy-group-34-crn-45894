[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/-cPJVYMd)
Django ORM Standalone
=====================
**Group 34: Assignment 3**

Sameer Karodia - 100918242

Sahil Asifi - 100914271

Sami Salah - 100827346

![Django](https://img.shields.io/badge/Django_ORM-Standalone-blue)
![Python](https://img.shields.io/badge/Python-yellow)

Use the database components of Django without having to use the rest of Django (i.e. running a web server)! :tada: A typical use case for using this template would be if you are writing a python script and you would like the database functionality provided by Django, but have no need for the request/response functionalty of a client/server web application that Django also provides.

With this project template you can write regular python scripts and use Django's excellent ORM functionality with the database backend of your choice. This makes it convienient for Djangonauts to write database driven python applications with the familiar and well polished Django ORM. Enjoy.

## :gear: Requirements

- Last tested successfully with Python 3.10.4 and Django 5.0.6
- Create venv and pip install django to import the required modules.

## :open_file_folder: File Structure

```
django-orm/
├── db/
│   ├── __init__.py
│   └── models.py
|   |__ views.py
├──templates
|   ├── db
|        ├──scan.html
├── main.py
├── manage.py
├── README.md
├── urls.py
└── settings.py
```

**Description Of Files:**

manage.py - The command-line entry point for the Django project. You use it to run the server, make migrations, and interact with Django.

settings.py - The main configuration file for the project — defines database settings, installed apps, template paths, middleware, etc.

urls.py - Maps web URLs (like /) to specific view functions (such as scan_view) that handle requests. It’s the project’s routing table.

main.py - The custom script to seed (populate) the database with product data.

**init**.py - Marks the folder as a Python package so Django can import it.

models.py - Defines the database structure — here we define the Product model with UPC, name, and price fields.

views.py - Contains logic for handling user requests and returning responses .

scan.html - The front-end HTML file rendered by views.py. It shows the input form for UPC scanning and displays product details.

**How to Run:**

python manage.py makemigrations db

python manage.py migrate

python main.py (to see database contents)

python manage.py runserver (to run with the UI and scan products)

**Successfull Screenshots:**
