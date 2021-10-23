from django.shortcuts import render, redirect
from .models import Talk
from django.db.models import Q

# Create your views here.

def talk_page(request):
    
    adopting=request.user.adopt.adopting.all()
    adopted=request.user.adopt.adopted.all()
    adopt=[]
    for i in adopting:
        adopt.append(i.id)
    for i in adopted:
        adopt.append(i.id)
    print(adopt)
    all=Talk.objects.filter(id__in=adopt)
    for i in all:
        print(i.id)
    return render(request,'talk.html',{'all':all})

def create_talk(request):
    talk=Talk()
    talk.body=request.POST['body']
    talk.writer=request.user
    talk.save()
    return redirect('conversation:talk_page')

def edit_talk(request,talk_id):
    edit_talk=Talk.objects.get(id=talk_id)
    return render(request, 'edit_talk.html',{'talk':edit_talk})


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
    
