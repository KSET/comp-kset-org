from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from zapisnici import views

urlpatterns = patterns('',
        url(r'^$', login_required(views.IndexView.as_view()), name='index'), # /zapisnici/
        url(r'^(?P<pk>\d+)/$', login_required(views.ZapisnikView.as_view()), name='zapisnik'), # /zapisnici/3
)
