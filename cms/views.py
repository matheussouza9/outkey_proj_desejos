# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cms.models import Desejo

@login_required
def index(request):
    return render(request, 'cms/index.html')

def list_desejos(request, desejo_id):
    desejo = get_object_or_404(Desejo, pk=desejo_id)

def show_desejo(request, desejo_id):
    desejo = get_object_or_404(Desejo, pk=desejo_id)

class UserLoginView(View):
    template_name = 'cms/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('cms_index')
            else:
                messages.error(request, 'Usuário inativo')
        else:
            messages.error(request, 'Credenciais inválidas')

        return render(request, self.template_name)

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout efetuado com sucesso')
    return redirect('cms_index')