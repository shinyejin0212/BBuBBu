from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
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
    if request.method =='POST':
        if request.POST['password1'] == request.POST['password2']:
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
            return redirect('user:login')
    else:
        res_data['error']='비밀번호가 다릅니다.'
    return render(request, 'signup.html',res_data)

#로그인
def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        User = auth.authenticate(username = username, password = password)
        print(User)
        if User is not None:
            auth.login(request, User)
            return redirect('user:test')
            
            #여기 main.html 연결시켜줘야함.

    return render(request, 'login.html')

#로그아웃
@login_required
def logout_view(request):
    auth.logout(request)
    return redirect('/')