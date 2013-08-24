from django.conf.urls import patterns, include, url
from utils.views import login
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^zapisnici/', include('minutes.urls', namespace="minutes")),
    url(r'^vijesti/', include('news.urls', namespace="news")),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^$', 'flatpage', {'url': '/'}, name='comp_home'), 
    url(r'^kontakt/$', 'flatpage', {'url': '/kontakt/'}, name='comp_kontakt'), 
)
