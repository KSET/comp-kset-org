from django.conf.urls import patterns, url

urlpatterns = patterns('minutes.views',
        url(r'^$', 'minutes_index'), # /minutes/
        url(r'^(?P<pk>\d+)/(?P<slug>[-\w\d]+)/$', 'minutes_detail', name='minutes'), # /minutes/3/zapisnik-21-03-2013/
)
