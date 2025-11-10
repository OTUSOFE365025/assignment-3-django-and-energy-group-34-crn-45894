############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """


#seed our Product model with upc codes,names and prices
# def seeding_values():
    
products=[
    {"upc":12345,"name":'Coffee',"price":8.32},
    {"upc":67890,"name":'Muffin',"price":2.50},
    {"upc":20318,"name":'Flour',"price":18.03},
    {"upc":67672,"name":'Apple',"price":1.99}
]
for p in products:
    Product.objects.get_or_create(upc=p["upc"],name=p["name"],price=p["price"])
        
for p in Product.objects.all():
    print(f'UPC: {p.upc} \t Name: {p.name} \t Price: {p.price}')


