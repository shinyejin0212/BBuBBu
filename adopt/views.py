from django.shortcuts import render
from user.models import User
# Create your views here.
from django.db.models import Q
from .models import Adopt

def main(request):
    return render(request,'main.html')

def adopt_try(request,id):
    
    mine=Adopt.objects.get(id=id)
    mine.applicant=True
    mine.save()

    want_adopt=Adopt.objects.filter(~Q(id=id))
    

    return render(request,'adopt.html')
    
