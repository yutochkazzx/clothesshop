from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .forms import CustomUserCreationForm


def signup(request):
    """
 РЕГИСТРАЦИЯ НОВОГО ПОЛЬЗОВАТЕЛЯ// ВЫДАЧА ОСНОВНЫХ ПРАВ
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): #ЕСЛИ ФОРМА ЗАПОЛНЕНА ПРАВИЛЬНО, ТО КОД ПРОДОЛЖАЕТСЯ
            user = form.save()
            login(request, user)
            return redirect('main:product_list')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


def logout_view(request):
    """
    Простой выход из аккаунта по GET-запросу.
    После выхода пользователь попадает на главную страницу.
    """
    logout(request)
    return redirect('main:product_list')
