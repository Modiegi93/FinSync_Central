from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.tables, name='tables'),
    re_path(r'^details/(?P<table_id>\d+)/$', views.details, name='table_details'),
    re_path(r'^create/$', views.create, name='create_table'),
    re_path(r'^create/(?P<workplace_uuid>.+)/$', views.create, name='create_table_with_params'),
    re_path(r'^delete/$', views.delete, name='delete_table'),
    re_path(r'^update/(?P<table_id>\d+)/$', views.update, name="update_table"),
    re_path(r'^(?P<workplace_uuid>.+)/(?P<page_num>\d+)/$', views.tables, name='tables_with_params'),
]
