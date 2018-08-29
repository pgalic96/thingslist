from django.conf.urls import url

from . import views

app_name = 'the_things_list'
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^create/$', views.CreateView.as_view(), name='create'),
    url(r'(?P<pk>[0-9]+)/$', views.ThingView.as_view(), name='thing-details'),
]
