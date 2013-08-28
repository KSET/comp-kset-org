from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('news.views',
        url(r'^$', 'news_index', name='index'), 
        url(r'^(?P<pk>\d+)/(?P<slug>[-\w\d]+)/$', 'news_detail', name='news'), 
)
