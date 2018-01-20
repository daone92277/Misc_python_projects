"""Defines URL patterns for learning_logs."""

from django.conf.urls import url

from . import views

urlpatterns = [
    #home page below
    url(r'^$', views.index, name = "index"),
    #Show all Topics
    url(r'^topics/$', views.topics, name = "topics"),

    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name = "topic"),
    #page for adding new topic 
    url(r'^new_topic/$', views.new_topic, name = "new_topic"),
    #page for adding a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name = "new_entry")
    #page for editing an entry 
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name = 'edit_entry'),

]
.