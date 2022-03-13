from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note
from django.forms import ModelForm, widgets


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label='Имя')
    last_name = forms.CharField(max_length=100, required=True, label='Фамилия')
    username = forms.CharField(max_length=100, required=True, label='Логин')
    email = forms.EmailField(max_length=100, required=True, label="Email", )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email')


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields =  ('full_text',)
        widgets = {'full_text':widgets.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Введите текст'})
                }