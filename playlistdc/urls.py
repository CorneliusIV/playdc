from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from .views import HomeView

urlpatterns = [
    # Examples:
    path('', HomeView.as_view(), name='home'),

    path('admin/rq/', include('django_rq.urls')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
