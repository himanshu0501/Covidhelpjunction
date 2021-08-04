from django.shortcuts import render

def homepage(request):
    return render(request,'covidhelpjunction/homepage.html')

