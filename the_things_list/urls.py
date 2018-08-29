from django.conf.urls import url

from . import views

app_name = 'the_things_list'
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='index'),
]
