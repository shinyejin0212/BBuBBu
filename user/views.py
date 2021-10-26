from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth
from .models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, "index.html")

def test(request):
    return render(request, 'test.html')


#회원가입
def signup_view(request):
    res_data = {}
    if request.method=='GET':
        return render(request,'signup.html')
    elif request.method =='POST':
        if request.POST['password1'] == request.POST['password2']:
            input_email=request.POST['email']
            if(input_email.split('@')[1]=='dongguk.edu'):
                user=User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    nickname=request.POST['nickname'],
                    name=request.POST['name'],
                    email=request.POST['email'],
                    department=request.POST['department'],
                    school_id=request.POST['school_id'],
                    is_dorm=request.POST['is_dorm'],
                    dorm_id=request.POST['dorm_id'],
                )
                user.save()
                auth.login(request,user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('index')
            else:
                return render(request, 'error.html')    
        else:
            res_data['error']='비밀번호가 다릅니다.'
        return render(request, 'signup.html',res_data)

#로그인
def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        User = auth.authenticate(username = username, password = password)
        
        if User is not None:
            auth.login(request, User)
            return redirect('index')
            
            #여기 main.html 연결시켜줘야함.

    return render(request, 'login.html')

#로그아웃
@login_required
def logout_view(request):
    auth.logout(request)
    return redirect('/')

def main(request):
    return render(request, "main.html")


#내 정보 보기
def profile(request,user_id):
    profile=User.objects.get(id=user_id)
    return render(request, 'profile.html',{'profile':profile})

def edit(request,user_id):
    profile=User.objects.get(id=user_id)
    return render(request,'edit.html',{'profile':profile})

def update_profile(request,user_id):
    profile=User.objects.get(id=user_id)
    
    if request.method =='POST':
        # print(request.FILES.get('photo'))
        # if request.FILES.get('photo'):
        #     profile.image=request.FILES['photo']
        profile.username=request.POST['username']
        profile.password1=request.POST['password1']
        profile.password2=request.POST['password2']
        profile.nickname=request.POST['nickname']
        profile.name=request.POST['name']
        profile.department=request.POST['department']
        profile.school_id=request.POST['school_id']
        profile.is_dorm=request.POST['is_dorm']
        if(profile.is_dorm=='no'):
            profile.dorm_id=''
        else:
            profile.dorm_id=request.POST['dorm_id']
        profile.save()
    return redirect('user:profile',profile.id)
        
      