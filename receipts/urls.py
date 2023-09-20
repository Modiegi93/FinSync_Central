from django.urls import path, re_path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    re_path(r'^$', views.receipts, name='receipts'),
    re_path(r'^details/(?P<receipt_id>\d+)/$', views.details, name='receipt_details'),
    re_path(r'^create/$', views.create, name='create_receipt'),
    re_path(r'^create/(?P<workplace_uuid>.+)/$', views.create, name='create_receipt_with_params'),
    re_path(r'^delete/$', views.delete, name='delete_receipt'),
    re_path(r'^update/(?P<receipt_id>.+)/$', views.update, name='update_receipt'),
    re_path(r'^(?P<workplace_uuid>.+)/(?P<page_num>\d+)/$', views.receipts, name='receipts_with_params'),
]
