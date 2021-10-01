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
    email = models.EmailField(max_length=20,default='')
    #이메일
    department=models.CharField(max_length=50, default='')
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
