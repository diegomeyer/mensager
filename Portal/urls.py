"""pnl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from pconsumer import views
from log import views as log_views

from django.contrib.auth import views as auth_view
from log.forms import LoginForm

urlpatterns = [
    url(r'^$', log_views.home, name='home'),
    url(r'^login/$', auth_view.login, {'template_name': 'log/login.html', 'authentication_form': LoginForm}, name='login'),

    url(r'^logout/$', views.my_logout, {'next_page': '/login'}),
    url(r'^admin/', admin.site.urls),
    url(r'^chat/$', views.chat),
    url(r'^chat1/$', views.chat1),
]
