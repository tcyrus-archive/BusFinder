from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'busapp.views.display_view', name='display_view'),
    url(r'^login$', 'busapp.views.login_view', name='login_view'),
    url(r'^modify$', 'busapp.views.modify_view', name='modify_view')
)
