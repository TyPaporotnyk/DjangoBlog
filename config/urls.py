from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    path('cookies/', views.cookies_view, name='cookies'),
    path('privacy/', views.privacy_view, name='privacy'),

    path('account/', include('src.account.urls')),
    path('blog/', include('src.blog.urls')),
]

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
