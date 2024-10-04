from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import *
from django.contrib.auth.forms import AuthenticationForm
from blog.settings import LOGIN_REDIRECT_URL
from .forms import UserRegistrationForm
from django.core.exceptions import PermissionDenied
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
User = get_user_model


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            context = {'title': 'Успешная регистраия', 'new_user': new_user}
            return render(request, 'users/register_done.html', context)
    user_form = UserRegistrationForm()
    context = {'title': 'регистраия', 'register_form': user_form}
    return render(request, 'users/register.html', context)

def log_in(request):
    form = AuthenticationForm(request,request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password )
        if user:
            login(request, user)
            url = request.GET.get('next', LOGIN_REDIRECT_URL)
            return redirect(url)
    context = {'form': form}
    return render(request, template_name='users/login.html', context=context)

def log_out(requst):
    logout(requst)
    return redirect('myblog:index')


@login_required()
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.user != user:
        return render
    context = {'user': user, 'title': 'Информация о профиле'}
    return render(request, template_name='user/profile.html', context=context)


def change_password(request):
    form = CustomPasswordChangeForm()
    if request.method == "POST":
        form = CustomPasswordChangeForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password_1']

            if request.user.check_password_password(old_password):
                request.user.set_pasword(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user)
                return redirect('myblog:index')
            else:
                form.add_error('old_password', 'Старый пароль неверный')
                return redirect('users:change_password')
    context = {'title': 'Сменить пароль', 'form':form}
    return render(request, template_name='users/change_password.html', context=context)


