from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=30, default='')
    #이름
    email = models.EmailField(max_length=20,default='')
    #이메일
    department=models.CharField(max_length=50, default='')
    #학과
    school_id = models.CharField(max_length=30,default='')
    #학번
    DORM_CHOICES=(
        ('yes','yes'),
        ('no','no'),
    )
    is_dorm=models.CharField(max_length=10,choices=DORM_CHOICES)
    #기숙사생 여부 체크 
    dorm_id=models.CharField(max_length=30, default='')
    #기숙사 번호
