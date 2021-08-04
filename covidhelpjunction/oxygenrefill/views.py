from django.shortcuts import render
import django_google_maps



# Create your views here.
def center(request):
    return render(request,'oxygenrefill/centerdetails.html')