from django.urls import path
from django.conf.urls import include
import authapp.views as authapp
from django.conf import settings
from mainapp import views as mainapp
from django.conf.urls.static import static
if settings.DEBUG:
    import debug_toolbar

app_name = 'authapp'


urlpatterns = [
    path('', mainapp.main, name='main'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('contact/', mainapp.contacts, name='contacts'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('basketapp/', include('basketapp.urls', namespace='basketapp')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)