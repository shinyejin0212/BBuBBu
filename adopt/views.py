from django.shortcuts import get_object_or_404, redirect, render
from user.models import User
# Create your views here.
from django.db.models import Q
from .models import Adopt

def adopt_main(request):
    return render(request,'adopt_main.html')

def adopt_try(request,id):
    
    mine=Adopt.objects.get(id=id)

    if mine.application==False:
        mine.application=True
        mine.save()

    want_adopt=Adopt.objects.filter(~Q(id=id)&Q(application=True)&Q(user__department=mine.user.department))
   
    return render(request,'adopt.html',{'want_adopt':want_adopt})
    
def adopting(request,id):
    user=User.objects.get(id=request.user.id)
    adopted_user = get_object_or_404(User,id=id)
    is_adopted=user.adopt in adopted_user.adopt.adopted.all()
    if is_adopted:
        user.adopt.adopting.remove(adopted_user.adopt)
    else:
        user.adopt.adopting.add(adopted_user.adopt)
    
  
    return redirect('adopt:adopt_try',request.user.id)