from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^init','MisBares.views.initialize'),
    url(r'^login', 'django.contrib.auth.views.login'),
    url(r'^logout', 'MisBares.views.logout_user'),
    url(r'^addBar', 'MisBares.views.addBar'),
    url(r'^chbar', 'MisBares.views.changeBar'),
    url(r'^images', 'MisBares.views.images'),
    url(r'^rates', 'MisBares.views.rates'),
    url(r'^comments', 'MisBares.views.comments'),
    url(r'^delcom', 'MisBares.views.deleteComments'),
    url(r'^bares', 'MisBares.views.bares')    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
