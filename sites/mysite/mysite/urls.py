"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from sitio import views as wmenu


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', wmenu.get_menu),
    url(r'^principal/', wmenu.get_principal),
    url(r'^json/', wmenu.set_json),
    url(r'^jmenu/', wmenu.get_menu),
    url(r'^jplanes/', wmenu.get_planes),
    url(r'^jinformacion/', wmenu.get_informacion),
    url(r'^index/', wmenu.get_index),
    url(r'^jcabeceras/', wmenu.get_cabeceras),
    url(r'^jpmenu/', wmenu.get_menu_principal),
]
