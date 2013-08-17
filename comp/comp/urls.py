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
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name='auth_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='auth_logout'),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^$', 'flatpage', {'url': '/'}, name='comp_home'), 
    url(r'^kontakt/$', 'flatpage', {'url': '/kontakt/'}, name='comp_kontakt'), 
)
