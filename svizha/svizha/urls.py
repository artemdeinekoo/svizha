from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
import rest_framework.urls
urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', include("items_service.urls")),
    path('', include("authentication.urls")),
    path('', include('rest_framework.urls', namespace='rest_framework')),
)
