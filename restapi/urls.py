from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView
)

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
    path('api/user/', include('user.urls'), name='user'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/product/', include('product.urls'), name='product'),

    # path('api/product', include('product.urls'), name='product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
