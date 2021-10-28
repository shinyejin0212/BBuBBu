from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth
import sys
sys.path.append("..")
from user.models import User
from django.db.models import Q
import random
# Create your views here.


def view_random(request, id):
    me=User.objects.get(id=id)
    if me.is_dorm == 'no':
        #기숙사 생이 아니면
        return render(request, 'dorm_error.html')

    me_id=int(me.dorm_id)
    floor=me_id//1000
    room=me_id%1000
    floor=str(floor)

    #others는 층수 같고, 내 방은 아닌 사람. dorm_id가 0은 아니어야함 공백도 아니어야함
    my_followers=me.d_followers.all()

    if not my_followers:
        #내 팔로워가 없으면
        others=User.objects.filter(Q(d_followers__isnull=True)&Q(dorm_id__startswith=floor)&~Q(dorm_id=me_id)&~Q(dorm_id=0)&~Q(dorm_id='')).order_by('?')[:5]
    else:
        #팔로워가 있으면
        others=User.objects.filter(Q(d_followers__isnull=True)&Q(dorm_id__startswith=floor)&~Q(dorm_id=me_id)&~Q(dorm_id=0)&~Q(dorm_id='')&~Q(username=my_followers[0].username)).order_by('?')[:5]
    return render(request, 'dorm_rand.html',{'others':others})

 
def follow(request, id):
    me=User.objects.get(id=request.user.id)
    target=User.objects.get(id=id)
    target.d_followers.add(me)
    return redirect('main')

