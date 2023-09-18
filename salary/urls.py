from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.salary, name='salary'),
    re_path(r'^details/(?P<salary_id>\d+)/$', views.details, name='salary_details'),
    re_path(r'^create/$', views.create, name='create_salary'),
    re_path(r'^create/(?P<company_uuid>.+)/$', views.create, name='create_salary_with_params'),
    re_path(r'^delete/$', views.delete, name='delete_salary'),
    re_path(r'^update/(?P<salary_id>\d+)$', views.update, name="update_salary"),
    re_path(r'^(?P<company_uuid>.+)/(?P<page_num>\d+)/$', views.salary, name='salary_with_params'),
]
