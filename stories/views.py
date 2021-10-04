from django.shortcuts import render

# Create your views here.

def storylist(request):
    return render(requesst,"storylist.html")

def detail(request):
    return render(request, "detail.html")