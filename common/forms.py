from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):   # UserCreationForm 를 상속받은 클래스
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")