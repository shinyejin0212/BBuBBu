from django.shortcuts import render,redirect
from django.contrib import auth
from user.models import User
from django.db.models import Q

#없으면 입양하라고 추천!
#근데 나보다 한 해 위의 사람이 있는데 이 사람이 이미 팔로워가 있으면 입양하라고 추천
def match_view(request,id):
    me=User.objects.get(id=id)
    up=str(int(me.school_id[:4])-1)
    other=User.objects.filter(Q(school_id__startswith=up)&Q(department=me.department)&Q(school_id__endswith=me.school_id[-3:]))
    if other:
        other[0].s_followers.add(me)
        return redirect("main")
    else:
        return render(request, 'match_error.html')
