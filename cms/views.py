# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from cms.forms import UserForm, RestrictedUserForm
from cms.models import Desejo

@login_required
def index(request):
    return render(request, 'cms/index.html')

@login_required
def list_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'cms/lista_usuarios.html', {'usuarios': usuarios})

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

class UserShowEditView(View):
    template_name = 'cms/show_edit.html'

    @method_decorator(login_required)
    def get(self, request, usuario_id):
        user = get_object_or_404(User, pk=usuario_id)

        if not request.user.is_superuser:
            form = RestrictedUserForm(instance=user)
            if user.id != request.user.id:
                messages.error(request, 'Somente os seus dados pessoais podem ser mostrados ou editados')
                return redirect(reverse('cms_show_edit_usuario', kwargs={'usuario_id': request.user.id}))
        else:
            form = UserForm(instance=user)

        return render(request, self.template_name, {'form': form, 'title': 'Editar Usuário'})

    @method_decorator(login_required)
    def post(self, request, usuario_id):
        user = get_object_or_404(User, pk=usuario_id)

        if not request.user.is_superuser:
            form = RestrictedUserForm(request.POST, instance=user)
            if user.id != request.user.id:
                messages.error(request, 'Somente os seus dados pessoais podem ser mostrados ou editados')
                return redirect(reverse('cms_show_edit_usuario', kwargs={'usuario_id': request.user.id}))
        else:
            form = UserForm(request.POST, instance=user)

        if form.is_valid():
            user = form.save(commit=False)


        return render(request, self.template_name, {'form': form})

@login_required
def list_desejos(request):
    if request.user.is_superuser:
        desejos = Desejo.objects.all()
    else:
        desejos = Desejo.objects.filter(dono=request.user)

    return render(request, 'cms/lista_desejos.html', {'desejos': desejos})