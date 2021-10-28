
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import auth
from user.models import User
from django.db.models import Q

#없으면 입양하라고 추천!
#근데 나보다 한 해 위의 사람이 있는데 이 사람이 이미 팔로워가 있으면 입양하라고 추천
def match_view(request,id):
    me=User.objects.get(id=id)
    up=str(int(me.school_id[:4])-1)
    other=User.objects.filter(Q(school_id__startswith=up)&~Q(id=id)&Q(department=me.department)&Q(school_id__endswith=me.school_id[-3:]))
    res_data={}
    if not other:
        return render('adopt_error.html')
    else:
        for i in other:
            i.s_followers.add(me)
            
        return redirect("stories:storylist")



 

