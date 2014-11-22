from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^init','MisBares.views.initialize'),
    url(r'^addBar', 'MisBares.views.addBar'),
    url(r'^(.*)', 'MisBares.views.bares')    
)
