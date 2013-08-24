from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from minutes.models import Minutes

@login_required
def index(request):
    template = 'minutes/index.html'
    minutes_list = Minutes.objects.order_by('-date')
    paginator = Paginator(minutes_list, 10)
    page = request.GET.get('page')
    try:
        minutes = paginator.page(page)
    except PageNotAnInteger:
        minutes = paginator.page(1)
    except EmptyPage:
        minutes = paginator.page(paginator.num_pages)

    return render(request, template, {'minutes_list': minutes})

@login_required
def detail(request, pk, slug):
    context = {'minutes': get_object_or_404(Minutes, pk=pk)}
    template = 'minutes/detail.html'
    return render(request, template, context)
