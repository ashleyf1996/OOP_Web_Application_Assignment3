from django.conf.urls import url
from . import views

urlpatterns = [
    # /entertainment_tonight/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /entertainment_tonight/info if someone writes 1 it saves it in s var called city id. 1-9+ this patt mathces any following ints

    url(r'^create/$', views.CreateEvent.as_view(), name='create'),
    url(r'login/$', views.Login.as_view(), name='login'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    url(r'^event/$', views.event, name='event'),
]

