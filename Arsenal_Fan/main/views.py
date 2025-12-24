from django.shortcuts import render
from news.models import News
from news.utils import paginate_news


def home(request):
    all_news = News.objects.filter(is_published=True)
    news = paginate_news(request, all_news, per_page=6)

    context = {
        'news': news,
        'next_match': {
            'opponent': 'Brighton and Hove Albion',
            'date': '27.12.2025',
            'time': '18:00',
            'competition': 'Premier League'
        }
    }
    return render(request, 'main/home.html', context)