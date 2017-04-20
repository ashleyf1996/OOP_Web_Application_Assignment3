#to let django know about the other url files

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^entertainment_tonight/', include('entertainment_tonight.urls')),
    url(r'^$', include('entertainment_tonight.urls')),


]

#Whenever were in developer mode, use these (url patterns)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)