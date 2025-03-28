from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth  import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User

# Create your views here.
def signup(request):
    if request.method == 'POST' :
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # hash함수: 어떠한 글자를 넣으면 그 글자를 특정글자로 바꿔주는 함수이다.
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'signup.html', context)

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())

            # /accounts/login/
            # /accounts/login/?next=/articles/create/
            next_url = request.GET.get('next')

            # next가 없을떄=>None or 'articles:index'
            # next가 있을떄 => 'articles/create' or 'articles:index'

            return redirect(next_url or 'articles:index')
    else:
        form = CustomAuthenticationForm()

    context = {
        'form' : form
    }
    return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


def profile(request, username):
    user_profile = User.objects.get(username = username)

    context = {
        'user_profile':user_profile
    }
    return render(request, 'profile.html', context)