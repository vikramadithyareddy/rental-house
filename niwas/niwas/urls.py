"""niwas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path,include,re_path

from account.views import user_login,index
from client.views import  home
from niwas import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('login/', user_login, name='login'),
    path('hosting/' , include('hostupload.urls')),
    path('account/', include("account.urls")),
    re_path(r'^accounts/', include('account.passwords.urls')),
    path('client_page1/' , include('client_page1.urls')),
    path('client_pages2/',include('client_pages2.urls')),
    path('client/',include('client.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
