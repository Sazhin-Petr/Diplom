from django.core.paginator import Paginator


def paginate_news(request, news_list, per_page=6):
    paginator = Paginator(news_list, per_page)
    page_number = request.GET.get('page', 1)
    return paginator.get_page(page_number)