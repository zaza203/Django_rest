from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('api/', include("bookShop.urls")),
    path('admin/', admin.site.urls),
]
