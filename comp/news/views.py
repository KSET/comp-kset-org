from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from models import News 

def news_index(request):
    template = 'news/index.html'
    news_list = News.objects.order_by('-date')
    paginator = Paginator(news_list, 10)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, template, {'news_list': news})

def news_detail(request, pk, slug):
    context = {'news': get_object_or_404(News, pk=pk)}
    template = 'news/detail.html'
    return render(request, template, context)
