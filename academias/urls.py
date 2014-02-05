from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
import os
admin.autodiscover()

site_media = os.path.join( 
    os.path.dirname(__file__),  'site_media' 
) 

urlpatterns = patterns('',
    url(r'^$','principal.views.index'),
    url(r'^index.html','principal.views.index'),    
    url(r'^services.html','principal.views.services'),
    url(r'^staff.html','principal.views.staff'),
    url(r'^consultations.html','principal.views.consultations'),
    url(r'^historia.html(?P<id>\d+)$','principal.views.historia'),
    url(r'^prices.html','principal.views.prices'),
    url(r'^contacts.html','principal.views.contacts'),
    url(r'^ws/json','principal.views.WsJson'),
    # Examples:
    # url(r'^$', 'recetario.views.home', name='home'),
    # url(r'^recetario/', include('recetario.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media}),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
)