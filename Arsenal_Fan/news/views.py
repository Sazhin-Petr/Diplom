from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import News, Comment
from .utils import paginate_news


def news_list(request):
    all_news = News.objects.filter(is_published=True)
    news = paginate_news(request, all_news, per_page=12)
    return render(request, 'news/news_list.html', {'news': news})


def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk, is_published=True)
    comments = news_item.comments.all()

    return render(request, 'news/news_detail.html', {
        'news': news_item,
        'comments': comments
    })


@login_required
def add_comment(request, pk):
    news_item = get_object_or_404(News, pk=pk)

    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(
                news=news_item,
                author=request.user,
                text=text
            )

    return redirect(f'/news/{pk}/')