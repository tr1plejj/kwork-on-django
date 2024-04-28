from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'profession', 'gender', 'first_name', 'last_name')


class ChangeProfileForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('avatar', 'email', 'exp', 'telegram', 'vk', 'about',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
