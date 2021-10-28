from django.shortcuts import render, redirect
from .models import Talk
from django.db.models import Q
from user.models import User
# Create your views here.

def talk_page(request):
    me = User.objects.get(id=request.user.id)

    adopting=me.adopt.adopting.all()
    adopted=me.adopt.adopted.all()
    adopt=[]
    adopti=[]
    adopte=[]

    for i in adopting:
        adopti.append(i.id)
    for i in adopted:
        adopte.append(i.id)
    for i in adopti:
        if i in adopte: #쌍방 팔로우 
            adopt.append(i)
    # print(adopt)

    mine=Talk.objects.filter(writer=request.user)# 내가쓴글

    pick= me.adopt.adopting.filter(id__in=adopt)
    
    all={}
    l=[]
    for i in pick:    #나랑 연결된애
        l.append(Talk.objects.filter(writer=i.user))
    all['adopt']=l

    dorm=[]
    dormpick=me.d_followers.all()
    dormpicked=me.d_followings.all()
    for i in dormpick:
        print(i.id)

    up=me.s_followings.all()
    down=me.s_followers.all()

    return render(request,'talk.html',{'all':all,'mine':mine})

def create_talk(request):
    talk=Talk()
    talk.body=request.POST['body']
    talk.writer=request.user
    talk.save()
    return redirect('conversation:talk_page')

def edit_talk(request,talk_id):
    edit_talk=Talk.objects.get(id=talk_id)

    adopting=request.user.adopt.adopting.all()
    adopted=request.user.adopt.adopted.all()
    adopt=[]
    adopti=[]
    adopte=[]
    for i in adopting:
        adopti.append(i.id)
    for i in adopted:
        adopte.append(i.id)
    for i in adopti:
        if i in adopte: #쌍방 팔로우 
            adopt.append(i)
    print(adopt)
  

    mine=Talk.objects.filter(writer=request.user)# 내가쓴글

    pick= request.user.adopt.adopting.filter(id__in=adopt)
    
    all=[]
    
    for i in pick:    #나랑 연결된애
        all.append(Talk.objects.filter(writer=i.user))

    return render(request, 'edit_talk.html',{'all':all,'mine':mine,'talk':edit_talk})


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
    
