

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls', namespace='core')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] +urlpatterns