from django.contrib import admin
from django.urls import path
from db.views import scan_view

urlpatterns = [
    path("", scan_view, name="scan"),
]
