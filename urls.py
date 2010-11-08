from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^en2photo/', include('en2photo.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # (r'^accounts/', include('registration.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
   #  (r'^photo/', include('photo.urls')),
     
     (r'^$', 'url.views.upload_view'),
     (r'^url/(?P<key>\w+/.+)/$', 'url.views.show_view'),
     (r'^(?P<key>\w+/.+)/$', 'url.views.direct_view'),
     
     
    
)




if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '%s/medias' % settings.PROJECT_PATH }),
        )

