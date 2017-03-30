from django.conf.urls import url
from . import views
from accounts.views import (login_view)
urlpatterns = [
    # /entertainment_tonight/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /entertainment_tonight/info if someone writes 1 it saves it in s var called city id. 1-9+ this patt mathces any following ints

    url(r'^create/$', views.home, name='create'),
    url(r'^login/$', login_view, name='login'),
]

