from .models import User
from django.contrib.auth.forms import UserCreationForm, forms
from main.models import Auto, Docs
from django.forms import ModelForm, TextInput, DateTimeInput


class UpdateUserForm(ModelForm):
    birth = forms.TextInput(attrs={
                'type':  'text',
                'placeholder': '',
                'id': "name-c6dc",
                'name': 'date',
                'size': "50",
                'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white'
            })
    class Meta:
        model = User
        fields = ['name', 'birth', 'number', 'email']

        widgets = {
            'name': TextInput(attrs={
                'type':  'text',
                'placeholder': '',
                'id': "name-c6dc",
                'name': 'name',
                'size': "50",
                'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white'
            }),
            'number': TextInput(attrs={
                'type': 'text',
                'placeholder': '',
                'id': "phone-ae12",
                'name': 'phone',
                'size': "50",
                'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white'
            }),
            'email': TextInput(attrs={
                'type': 'email',
                'placeholder': '',
                'id': "email-c012",
                'name': 'email',
                'size': "50",
                'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white'
            }),
        }

class UpdateAutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = ['model', 'year', 'vin']

        widgets = {
            'model': TextInput(attrs={
                'type': "text",
                'placeholder': "",
                'id': "text-c7dc",
                'name': "model",
                'class': "u-border-1 u-border-grey-30 u-input u-input-rectangle u-white",
                'size': "50"
            }),
            'year': TextInput(attrs={
                'type': "text",
                'placeholder': "",
                'id': "text-c7dc",
                'name': "year",
                'class': "u-border-1 u-border-grey-30 u-input u-input-rectangle u-white",
                'size': "50"
            }),
            'vin': TextInput(attrs={
                'type': "text",
                'placeholder': "",
                'id': "text-c7dc",
                'name': "vin",
                'class': "u-border-1 u-border-grey-30 u-input u-input-rectangle u-white",
                'size': "50"
            }),
        }

class UpdateDocsForm(ModelForm):
    class Meta:
        model = Docs
        fields = ['model', 'ctc', 'policy', 'license']

        widgets = {
            'model': TextInput(attrs={
                'type': "text",
                'placeholder': "",
                'id': "text-c7dc",
                'name': "model",
                'class': "u-border-1 u-border-grey-30 u-input u-input-rectangle u-white",
                'size': "50"
            }),
            'ctc': TextInput(attrs={
                'type': "text",
                'placeholder': "",
                'id': "text-c7dc",
                'name': "year",
                'class': "u-border-1 u-border-grey-30 u-input u-input-rectangle u-white",
                'size': "50"
            }),
            'policy': TextInput(attrs={
                'type': "text",
                'placeholder': "",
                'id': "text-c7dc",
                'name': "vin",
                'class': "u-border-1 u-border-grey-30 u-input u-input-rectangle u-white",
                'size': "50"
            }),
            'license': TextInput(attrs={
                'type': "text",
                'placeholder': "",
                'id': "text-c7dc",
                'name': "vin",
                'class': "u-border-1 u-border-grey-30 u-input u-input-rectangle u-white",
                'size': "50"
            }),
        }