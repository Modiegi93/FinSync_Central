from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name='alert_and_redirect.html'), name='logout'),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^password/$', views.change_password, name='change_password'),
]
