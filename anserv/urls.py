from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dashboard.views.dashboard'),
    url(r'^event$', 'an_evt.views.handle_event'),
    url(r'^view/([A-Za-z_+]+)/([A-Za-z_+]+)$', 'an_evt.views.handle_view'),
    url(r'^view/([A-Za-z_+]+)/([A-Za-z_+]+)/([A-Za-z_0-9]+)$', 'an_evt.views.handle_view'),
    url(r'^view/([A-Za-z_+]+)/([A-Za-z_+]+)/([A-Za-z_0-9]+)/([A-Za-z_0-9]+)$', 'an_evt.views.handle_view'),
    url(r'^query/([A-Za-z_+]+)/([A-Za-z_+]+)$', 'an_evt.views.handle_query'),
    url(r'^query/([A-Za-z_+]+)/([A-Za-z_+]+)/([A-Za-z_0-9+]+)$', 'an_evt.views.handle_query'),
    url(r'^query/([A-Za-z_+]+)/([A-Za-z_+]+)/([A-Za-z_0-9+]+)/([A-Za-z_0-9+]+)$', 'an_evt.views.handle_query'),
    url(r'^probe$', 'an_evt.views.handle_probe'),
    url(r'^probe/([A-Za-z_+]+)$', 'an_evt.views.handle_probe'),
    url(r'^probe/([A-Za-z_+]+)/([A-Za-z_+]+)$', 'an_evt.views.handle_probe'),
    url(r'^probe/([A-Za-z_+]+)/([A-Za-z_+]+)/([A-Za-z_+]+)$', 'an_evt.views.handle_probe'),
    url(r'^probe/([A-Za-z_+]+)/([A-Za-z_+]+)/([A-Za-z_+]+)/([A-Za-z_+]+)$', 'an_evt.views.handle_probe'),
    url(r'^dashboard$', 'dashboard.views.dashboard'),
    # url(r'^anserv/', include('anserv.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^frontend/', include('frontend.urls')),
    url('^tasks/', include('djcelery.urls')),
)

if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
    urlpatterns+= patterns('',
                           url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
                               'document_root': settings.STATIC_ROOT,
                               'show_indexes' : True,
                               }),
                           )

handler404 = 'error_templates.render_404'
handler500 = 'error_templates.render_500'

