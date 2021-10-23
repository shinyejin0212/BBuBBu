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

    # adopt라는 리스트에 입양되거나 입양하는 애들 id값담아서 아래서에서 filter로 걔내가 쓴글 다가져와서 보이게해줄거임
    # 뻔선뻔후, 긱사도 여기서 다 append하고 template으로 넘기기
    # 단체톡방느낌으로 다른사람이 쓴건 그사람이름, 올린시간, 내용 왼쪽에, 내가쓴건 오른쪽에, 시간순 orderby해서 대화형식처럼 ㅇㅇ

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
    
