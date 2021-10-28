from django.shortcuts import render, redirect
from .models import Talk
from django.db.models import Q
from user.models import User
# Create your views here.

def talk_page(request):
    me = User.objects.get(id=request.user.id)

    adopting=me.adopt.adopting.all()
    adopted=me.adopt.adopted.all()
    adopti=[]
    adopte=[]
    for i in adopting:
        adopti.append(i.id)
    for i in adopted:
        adopte.append(i.id)
    
    a=set(adopti)
    b=set(adopte)
    adopt=a&b # 쌍방 입양
    
    dorm=[]
    dormpick=me.d_followers.all()
    dormpicked=me.d_followings.all()
    for i in dormpick:
        dorm.append(i.id)
    for i in dormpicked:
        dorm.append(i.id)
    dorm_set=set(dorm)


    num=[]
    up=me.s_followings.all()
    down=me.s_followers.all()
    for i in up:
        num.append(i.id)
    for i in down:
        num.append(i.id)
    num_set=set(num)

    mid=me.id
    me_set=set([mid])
    
    all=adopt|dorm_set|num_set|me_set

    l_all=list(all)

    
    pick= User.objects.filter(id__in=l_all)
    
    l=Talk.objects.filter(writer__in=pick).order_by('updated_at')

    return render(request,'talk.html',{'l':l,'num':num,'adopt':list(adopt),'dorm':dorm,'me':me})

def create_talk(request):
    talk=Talk()
    talk.body=request.POST['body']
    talk.writer=request.user
    talk.save()
    return redirect('conversation:talk_page')

def edit_talk(request,talk_id):
    edit_talk=Talk.objects.get(id=talk_id)
    me = User.objects.get(id=request.user.id)

    adopting=me.adopt.adopting.all()
    adopted=me.adopt.adopted.all()
    adopti=[]
    adopte=[]
    for i in adopting:
        adopti.append(i.id)
    for i in adopted:
        adopte.append(i.id)
    
    a=set(adopti)
    b=set(adopte)
    adopt=a&b # 쌍방 입양
    
    dorm=[]
    dormpick=me.d_followers.all()
    dormpicked=me.d_followings.all()
    for i in dormpick:
        dorm.append(i.id)
    for i in dormpicked:
        dorm.append(i.id)
    dorm_set=set(dorm)


    num=[]
    up=me.s_followings.all()
    down=me.s_followers.all()
    for i in up:
        num.append(i.id)
    for i in down:
        num.append(i.id)
    num_set=set(num)

    mid=me.id
    me_set=set([mid])
    
    all=adopt|dorm_set|num_set|me_set

    l_all=list(all)

    
    pick= User.objects.filter(id__in=l_all)
    
    l=Talk.objects.filter(writer__in=pick).order_by('updated_at')

    return render(request,'edit_talk.html',{'l':l,'num':num,'adopt':list(adopt),'dorm':dorm,'me':me,'talk':edit_talk})



def update_talk(request,talk_id):
    update_talk=Talk.objects.get(id=talk_id)
    update_talk.body=request.POST['body']
    update_talk.writer=request.user
    update_talk.save()
    return redirect('conversation:talk_page')

   
def delete_talk(request,talk_id):
    
    delete_talk = Talk.objects.get(id=talk_id)
    delete_talk.delete()
    return redirect('conversation:talk_page')
    
