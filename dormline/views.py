from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth
import sys
sys.path.append("..")
from user.models import User
from django.db.models import Q
import random
# Create your views here.

def dorm_main(request):
    followers=request.user.d_followers
    return render(request, 'dorm_main.html',{'followers':followers})

def view_random(request, id):
    me=User.objects.get(id=id)
    me_id=int(me.dorm_id)
    floor=me_id//1000
    room=me_id%1000
    floor=str(floor)
    #내 층이랑 방 호수 받았음.
    others=User.objects.filter(Q(d_followers__isnull=True)&Q(dorm_id__startswith=floor)&~Q(dorm_id=me_id)&~Q(dorm_id=0)&~Q(dorm_id='')&~Q(d_followings__in=[request.User]))
    #others는 층수 같고, 내 방은 아닌 사람
    #dorm_id가 0은 아니어야함 공백도 아니어야함
    #팔로워도 없어야한다. 
    #나를 팔로잉 하는 것도 아니어야함

    random.seed(1)
    li=[x for x in range(len(others))]
    if len(others)<5:
        choice_list=li
    else:
        choice_list=random.sample(li, 5)

    return render(request, 'dorm_rand.html',{'others':others})

 
def follow(request, id):
    me=User.objects.get(id=request.user.id)
    target=User.objects.get(id=id)
    target.d_followers.add(me)
    return redirect('dormline:dorm_main')

