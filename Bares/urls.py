from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^init','MisBares.views.initialize'),
    url(r'^login', 'django.contrib.auth.views.login'),
    url(r'^logout', 'MisBares.views.logout_user'),
    url(r'^addBar', 'MisBares.views.addBar'),
    url(r'^upload', 'MisBares.views.upload'),
    url(r'^(.*)', 'MisBares.views.bares')    
)
