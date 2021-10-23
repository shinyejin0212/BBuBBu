

from django.shortcuts import render,redirect, get_object_or_404
from user.models import User
from django.db.models import Q



def matching_view(request):
    user_id=request.user.id
    mine = User.objects.get(id=user_id)
    print(mine.school_id[-3:])
    all=User.objects.filter(Q(school_id__endswith=mine.school_id[-3:]))

    for i in all:
        print(i.school_id)


    return render(request, "")

