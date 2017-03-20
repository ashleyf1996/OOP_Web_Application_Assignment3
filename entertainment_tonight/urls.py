from django.conf.urls import url
from . import views

urlpatterns = [
    # /entertainment_tonight/
    url(r'^$', views.index, name='index'),

    # /entertainment_tonight/info if someone writes 1 it saves it in s var called city id. 1-9+ this patt mathces any following ints

    url(r'^(?P<cities_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'city/add/$', views.CitiesCreate.as_view(),name='city-add')
]
