from django.urls import path, re_path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    re_path(r'^$', lambda r: redirect('/companies/1+1/')),
    re_path(r'^(?P<workplaces_page_num>\d+)\+(?P<owned_companies_page_num>\d+)/$', views.companies, name='companies'),
    re_path(r'^create/$', views.create, name='create_company'),
    re_path(r'^join/$', views.join, name='join_company'),
    re_path(r'^delete/$', views.delete, name='delete_company'),
    re_path(r'^fire/$', views.fire_staff, name='fire_employee'),
    re_path(r'^quit/$', views.leave, name='quit_company'),
    re_path(r'^manage/(?P<company_uuid>.+)/$', views.render_staff_page, name='manage_staff'),
    re_path(r'^update/(?P<company_uuid>.+)/$', views.update, name='update_company'),
    re_path(r'^details/(?P<company_uuid>.+)/$', views.details, name='company_details'),
]
