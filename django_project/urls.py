from django.conf.urls import patterns, include, url

from django.contrib import admin
from BotApp import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',  views.index),
    url(r'^reg/$', views.reg),
)
