#to let django know about the other url files

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),


    url(r'^entertainment_tonight/', include('entertainment_tonight.urls')),

]
