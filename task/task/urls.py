from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
admin.autodiscover()
admin.site.enable_nav_sidebar = False
from django.views.static import serve
	
urlpatterns = [
    path('', include('demo.urls')),
    path('admin/', admin.site.urls),
    url(r'^', include('api.urls')),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)