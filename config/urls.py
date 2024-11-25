from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import handler404
# model translation
from django.conf.urls.i18n import i18n_patterns
from .errors import custom_page_not_found_view

urlpatterns = [] + i18n_patterns (
    # i18n qo'shish bu oxiriga uz, ru, en v h k qoshib beradi
    path('modelview/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('app.urls')),
    path('api/', include('app.api_urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = custom_page_not_found_view