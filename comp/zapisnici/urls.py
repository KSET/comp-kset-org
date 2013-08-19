from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from zapisnici import views

urlpatterns = patterns('',
        url(r'^$', views.IndexView.as_view()), # /zapisnici/
        url(r'^(?P<pk>\d+)/$', views.ZapisnikView.as_view(), name='zapisnik'), # /zapisnici/3
)
