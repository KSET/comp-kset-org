from django.conf.urls import patterns, url
from zapisnici import views

urlpatterns = patterns('',
        url(r'^$', views.IndexView.as_view(), name='index'), # /zapisnici/
        url(r'^(?P<pk>\d+)/$', views.ZapisnikView.as_view(), name='zapisnik'), # /zapisnici/3
)
