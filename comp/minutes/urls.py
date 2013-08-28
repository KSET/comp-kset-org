from django.conf.urls import patterns, url

urlpatterns = patterns('minutes.views',
        url(r'^$', 'minutes_index', name='index'), # /minutes/
        url(r'^(?P<pk>\d+)/(?P<slug>[-\w\d]+)/$', 'minutes_detail', name='details'), # /minutes/3/zapisnik-21-03-2013/
)
