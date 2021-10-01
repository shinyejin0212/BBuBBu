from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import UserProfile
# Register your models here.


class SignupForm(forms.Form):
    class Meta:
        model=User
    
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':''}),label="이름")
    department = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'ex)산업시스템공학과'}),label="학과")
    school_id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':''}), label="학번")
    DORM_CHOICES=(
        ('yes','yes'),
        ('no','no'),
    )
    is_dorm=forms.ChoiceField(choices=DORM_CHOICES,label='기숙사생여부',widget=forms.Select)
    dorm_id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':''}), label="기숙사번호")
    
    def signup(self, request, user):
        userProfile=UserProfile()
        userProfile.user=user
        userProfile.name=self.cleaned_data[('name')]
        userProfile.email=user.email
        userProfile.department=self.cleaned_data[('department')]
        userProfile.school_id=self.cleaned_data[('school_id')]
        userProfile.is_dorm=self.cleaned_data[('is_dorm')]
        userProfile.dorm_id=self.cleaned_data[('dorm_id')]
        userProfile.save()
        user.save()
        return user
