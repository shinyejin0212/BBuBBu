from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import auth
from user.models import User
# from .models import Match


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
    






