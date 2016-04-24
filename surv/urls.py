from django.conf.urls import patterns, include, url
from django.contrib import admin
from surv.views import home
urlpatterns = patterns('',
    # Examples:
    url(r'^$', home.as_view(), name='home'),
    url(r'^api/sms/incoming/$', home.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
