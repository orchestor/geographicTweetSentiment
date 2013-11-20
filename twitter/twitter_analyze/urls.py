from django.conf.urls import patterns, url

from twitter_analyze import views

urlpatterns = patterns('',url(r'^(?P<query>\w+)/$', views.index, name='index'),url(r'^search-form/$', views.search_form))
