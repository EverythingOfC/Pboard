from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일') # 이메일 필드 객체 생성

    class Meta:
        model = User # User모델을 사용함.
        fields = ("username","password1","password2","email") # User모델의 속성들