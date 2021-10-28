<<<<<<< HEAD
=======

>>>>>>> d0ad08e104a459472ccb83f94a842f08bad92073
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import auth
from user.models import User
# from .models import Match

#없으면 입양하라고 추천!
#근데 나보다 한 해 위의 사람이 있는데 이 사람이 이미 팔로워가 있으면 입양하라고 추천
def match_view(request,id):
    me=User.objects.get(id=id)
    up=str(int(me.school_id[:4])-1)
    other=User.objects.get(Q(school_id__startswith=up)&~Q(id=id)&Q(department=me.department)&Q(school_id__endswith=me.school_id[-3:]))
    
    res_data={}
    if other:
        other.s_followers.add(me)
        print(other.username)
        print(other.s_followers.name)

<<<<<<< HEAD
def match_main(request):
    followers=request.user.s_followers
    followings=request.user.s_followings
    return render(request,'match.html',{'followers':followers} )


def match_view(request):
    user_id = request.user.id
    followers=request.user.s_followers
    mine = User.objects.get(id=user_id)
    upline = int(mine.school_id[:4]) - 1

    #학과, 학번 뒤 세자리 동일, 자신은 제외
    all=User.objects.filter(department = mine.department, school_id__endswith=mine.school_id[-3:],school_id__startswith=upline).exclude(school_id=mine.school_id)
    
    for i in all:
        # i.username = 
        print(i.school_id, i.name)
        school_upline = i
        

    def school_follow(request, id):
        me=User.objects.get(id=request.user.id)
        s_followed_user = school_upline 
        is_follower = user.user in s_followed_user.user.s_followers.all()

        #팔로워 목록 존재하지 않을 시 입양으로 연결
        #
        #
        #
    return render(request, 'match.html', {'followers': school_upline})
    





=======
        return redirect("stories:list")
    else:
        return render('adopt_error.html')
        



 
>>>>>>> d0ad08e104a459472ccb83f94a842f08bad92073

