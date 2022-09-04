from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, 'users/index.html')


def add_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            print('User added. OK')
    else:
        user_form = UserForm()
    return render(request, 'user/sign_in.html')

