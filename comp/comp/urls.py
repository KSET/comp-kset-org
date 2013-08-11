from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'comp.views.home', name='home'),
    # url(r'^comp/', include('comp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^zapisnici/', include('zapisnici.urls', namespace="zapisnici")),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='comp_about'), 
    url(r'^kontakt/$', 'flatpage', {'url': '/kontakt/'}, name='comp_kontakt'), 
)
