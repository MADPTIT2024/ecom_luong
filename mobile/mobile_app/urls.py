from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, MobileViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'mobiles', MobileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]