from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'index.html', context)


@login_required # 아래 있는 함수를 실행하기 전에 @함수를 먼저 실행 시켜 주세요
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')

    else:
        form = ArticleForm()

    context = {
        'form':form,
    }
    return render(request, 'create.html', context)