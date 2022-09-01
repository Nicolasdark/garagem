from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from core.serializers import CarroSerializer

from core.views import MarcaViewSet, CategoriaViewSet, CarroViewSet

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"carros", CarroViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
