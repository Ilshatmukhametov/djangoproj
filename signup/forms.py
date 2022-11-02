from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput

class CreateUserForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white', 'type':'password', 'placeholder':'Пароль', 'name':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white', 'type':'password', 'placeholder':'Повторите пароль'}),
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            "username": TextInput(attrs={
                'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white',
                'placeholder': 'Логин'
            }),
            "email": TextInput(attrs={
                'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white',
                'placeholder': 'Email'
            }),

        }