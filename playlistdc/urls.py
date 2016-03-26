from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'playlistdc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/rq/', include('django_rq.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
