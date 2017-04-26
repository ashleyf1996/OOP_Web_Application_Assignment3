from django.conf.urls import url
from . import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # /entertainment_tonight/
    # These are the urls for my website

    url(r'^$', views.index.as_view(), name='index'),
    url(r'^create/$', views.CreateEvent.as_view(), name='create'),
    url(r'^about/$', views.About.as_view(), name='about'),
    url(r'^event/delete-event/(?P<id>[0-9]+)/$', views.DeleteEvent.as_view(), name='delete-event'),

    url(r'login/$', views.Login.as_view(), name='login'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    url(r'^event/$', views.EventView.as_view(), name='event'),
    url(r'^city/$', views.city, name='city'),


]

