from django.shortcuts import render

# Create your views here.

def dorm_main(request):
    render(request, 'dorm_main.html')