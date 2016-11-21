# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, CheckboxInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'is_active', 'is_superuser']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'Nome de usuário',
            'first_name': 'Primeiro nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
            'password': 'Senha',
            'is_active': 'Ativo',
            'is_superuser': 'Tornar administrador',
        }
        help_texts = {
            'username': '',
            'is_active': '',
            'is_superuser': '',
        }
        error_messages = {

        }

class RestrictedUserForm(UserForm):
    class Meta(UserForm.Meta):
        exclude = ['is_active', 'is_superuser']