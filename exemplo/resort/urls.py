from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from quartos.api import QuartoViewSet

router = DefaultRouter()
router.register('quartos', QuartoViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quartos.urls')),
    path('api/', include(router.urls)),
]
