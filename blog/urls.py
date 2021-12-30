from django.conf.urls import include
from django.db import router
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()

router.register('category', CategoryViewSet, 'category')
router.register('admin/category', CategoryAdminViewSet, 'admin-category')

urlpatterns = [
    path('', include(router.urls))
]
