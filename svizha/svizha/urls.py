from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += i18n_patterns(
    path('', include("items_service.urls")),
    path('', include("authentication.urls")),
)
