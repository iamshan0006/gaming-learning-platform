from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('content/', include('content.urls')),
    path('gameplay/', include('gameplay.urls')),
    path('analytics/', include('analytics.urls')),
    path('classroom/', include('classroom.urls')),
]

