from django.shortcuts import render
from django import forms
from .models import Product

# Simple form for entering/scanning a UPC
class UPCScanForm(forms.Form):
    upc = forms.CharField(label="Scan or Enter UPC", max_length=32)

def scan_view(request):
    form = UPCScanForm(request.POST or None)
    product = None
    not_found = False

    if request.method == "POST" and form.is_valid():
        upc = form.cleaned_data["upc"].strip()
        try:
            product = Product.objects.get(upc=upc)
        except Product.DoesNotExist:
            not_found = True

    return render(request, "db/scan.html", {
        "form": form,
        "product": product,
        "not_found": not_found,
    })
