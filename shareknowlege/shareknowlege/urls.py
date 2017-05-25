"""shareknowlege URL Configuration

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
from shareapp import views as appview

from haystack.views import SearchView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', appview.index),
    url(r'^login', appview.login),
    url(r'^register', appview.register),
    url(r'^editor', appview.editor),
    url(r'^addtext', appview.addtext),
    url(r'^view', appview.view),
    url(r'^search', SearchView(), name='haystack_search'),
    url(r'^logout', appview.logout),
    url(r'^adminhome', appview.admin),
    url(r'^delete', appview.delete),
    url(r'username', appview.usernamedelete),
    url(r'^homelook', appview.homesearch),
    url(r'^addcoment', appview.addcomment),

]
