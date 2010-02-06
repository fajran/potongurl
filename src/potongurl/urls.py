from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^\+media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^\+admin/', include(admin.site.urls)),
    (r'(?P<hash>[a-zA-Z0-9]+)$', 'potongurl.views.go'),
    (r'^$', 'potongurl.views.index'),
)
