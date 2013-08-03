from django.http import HttpResponse
from zapisnici.models import Zapisnik
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'zapisnici/index.html'

    def get_queryset(self):
        return Zapisnik.objects.order_by('-zap_date')[:5]

class ZapisnikView(generic.DetailView):
    model = Zapisnik
