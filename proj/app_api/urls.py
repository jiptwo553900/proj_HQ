from rest_framework import routers
from django.urls import path, include

from proj.app_api.views import UserViewSet, ProductViewSet, LessonViewSet, LessonHistoryViewSet, LessonsDetailsForUser, ProductDetailsForUser


router = routers.DefaultRouter()
router.register(prefix=r'users', viewset=UserViewSet, basename='users')
router.register(prefix=r'products', viewset=ProductViewSet, basename='products')
router.register(prefix=r'lessons', viewset=LessonViewSet, basename='lessons')
router.register(prefix=r'lesson-history', viewset=LessonHistoryViewSet, basename='lesson-history')
router.register(prefix=r'lesson-history-for-user', viewset=LessonsDetailsForUser, basename='lesson-history-for-user')
router.register(prefix=r'product-details-for-user', viewset=ProductDetailsForUser, basename='product-details-for-user')


urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls
