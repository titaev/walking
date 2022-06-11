from django.shortcuts import render
from .forms import UserRegistrationForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        data = UserRegistrationForm(request.POST)
        if data.is_valid():
            new_user = data.save(commit='False')
            new_user.set_password(data.cleaned_data['password'])
            new_user.save()
            login(request)
            return HttpResponseRedirect('/')
    user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/accounts/login')
    return render(request, 'accounts/login.html')


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def delete_acc(request):
    curent_user = request.user
    user = User.objects.get(id=curent_user.id)
    user.delete()
    return HttpResponseRedirect('/')
