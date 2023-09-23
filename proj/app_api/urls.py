from rest_framework import routers
from django.urls import path, include

from .views import (
    UserViewSet,
    ProductViewSet,
    LessonViewSet,
    LessonHistoryViewSet,
)


router = routers.DefaultRouter()
router.register(prefix=r'users', viewset=UserViewSet)
router.register(prefix=r'products', viewset=ProductViewSet)
router.register(prefix=r'lessons', viewset=LessonViewSet)
router.register(prefix=r'lesson_history', viewset=LessonHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]