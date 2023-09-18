"""
URL configuration for finsync project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path, re_path
from django.contrib import admin
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', lambda r: redirect('/index/')),
    re_path(r'^index/', include('index.urls')),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^companies/', include('companies.urls')),
    re_path(r'^info/', include('info.urls')),
    re_path(r'^receipts/', include('receipts.urls')),
    re_path(r'^tables/', include('tables.urls')),
    re_path(r'^tax/', include('tax.urls')),
    re_path(r'^salary/', include('salary.urls')),
    re_path(r'^admin/', admin.site.urls),
]

# For serving static files even not in debug mode...
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
elif getattr(settings, 'FORCE_SERVE_STATIC', False):
    settings.DEBUG = True
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    settings.DEBUG = False
