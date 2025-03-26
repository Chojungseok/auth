from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
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