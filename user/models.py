from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User,BaseUserManager,AbstractBaseUser,PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, nickname, password, name, email, department, school_id, is_dorm, dorm_id):
        user=self.model(
            username=username,
            nickname=nickname,
            name=name,
            email=email,
            department=department,
            school_id=school_id,
            is_dorm=is_dorm,
            dorm_id=dorm_id,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, nickname, username, password):
        user=self.create_user(
            username=username,
            nickname=nickname,
            password=password,
            name='',
            email='',
            department='',
            school_id=0,
            is_dorm=True,
            dorm_id=0,
        )
        user.set_password(password)
        user.is_admin=True
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user
    

 

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, default='')
    #아이디
    nickname = models.CharField(max_length=100, unique=True, default='')
    #닉네임
    name=models.CharField(max_length=30, default='')
    #이름
    email = models.EmailField(max_length=30,default='')
    #이메일
    CHOICE_DEPART=(
        ('AI융합학부','AI융합학부'),
        ('가정교육과','가정교육과'),
        ('건설환경공학과','건설환경공학과'),
        ('건축공학부','건축공학부'),
        ('경영정보학과','경영정보학과'),
        ('경영학과','경영학과'),
        ('경제학과','경제학과'),
        ('경찰행정학부','경찰행정학부'),
        ('광고홍보학과','광고홍보학과'),
        ('교육학과','교육학과'),
        ('국어교육과','국어교육과'),
        ('국어국문학전공','국어국문학전공'),
        ('국제통상학과','국제통상학과'),
        ('글로벌무역학과','글로벌무역학과'),
        ('기계로봇에너지공학과','기계로봇에너지공학과'),
        ('멀티미디어공학과','멀티미디어공학과'),
        ('문예창작학전공','문예창작학전공'),
        ('물리학전공','물리학전공'),
        ('뮤지컬전공','뮤지컬전공'),
        ('미디어커뮤니케이션학전공','미디어커뮤니케이션학전공'),
        ('바이오환경과학과','바이오환경과학과'),
        ('반도체과학전공','반도체과학전공'),
        ('법학과','법학과'),
        ('북한학전공','북한학전공'),
        ('불교미술전공','불교미술전공'),
        ('불교학부','불교학부'),
        ('사학과','사학과'),
        ('사회복지상담학과','사회복지상담학과'),
        ('사회복지학과','사회복지학과'),
        ('사회학전공','사회학전공'),
        ('산업시스템공학과','산업시스템공학과'),
        ('생명과학과','생명과학과'),
        ('서양화전공','서양화전공'),
        ('수학과','수학과'),
        ('수학교육과','수학교육과'),
        ('스포츠문화학과','스포츠문화학과'),
        ('식품산업관리학과','식품산업관리학과'),
        ('식품생명공학과','식품생명공학과'),
        ('약학과','약학과'),
        ('역사교육과','역사교육과'),
        ('연극전공','연극전공'),
        ('영어문학전공','영어문학전공'),
        ('영어통번역학전공','영어통번역학전공'),
        ('영화영상학과','영화영상학과'),
        ('윤리문화학전공','윤리문화학전공'),
        ('융합보안학과','융합보안학과'),
        ('융합에너지신소재공학과','융합에너지신소재공학과'),
        ('의생명공학과','의생명공학과'),
        ('일본학과','일본학과'),
        ('전자전기공학부','전자전기공학부'),
        ('정보통신공학전공','정보통신공학전공'),
        ('정치외교학전공','정치외교학전공'),
        ('조소전공','조소전공'),
        ('중어중문학과','중어중문학과'),
        ('지리교육과','지리교육과'),
        ('철학과','철학과'),
        ('체육교육과','체육교육과'),
        ('컴퓨터공학전공','컴퓨터공학전공'),
        ('통계학과','통계학과'),
        ('한국화전공','한국화전공'),
        ('행정학전공','행정학전공'),
        ('화공생물공학과','화공생물공학과'),
        ('화학과','화학과'),
        ('회계학과','회계학과')
    )
    department=models.CharField(max_length=50, choices=CHOICE_DEPART,default='')
    #학과
    school_id = models.CharField(max_length=30,default='')
    #학번
    is_dorm=models.CharField(max_length=10,default='')
    #기숙사생 여부 체크 
    dorm_id=models.CharField(max_length=30, default='')
    #기숙사 번호

    objects=UserManager()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['nickname']

    def __str__(self):
        return self.username
