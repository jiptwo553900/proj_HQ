from django.urls import path, include
from rest_framework import routers

from proj.app_api.views import UserLessonsViewSet, UserLessonsByProductViewSet, ProductStatisticsViewSet

router = routers.DefaultRouter()
router.register('lessons-by-user', UserLessonsViewSet, 'lessons-by-user')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'lessons-by-product/<int:product_id>/',
        UserLessonsByProductViewSet.as_view({'get': 'list'})
    ),
    path(
        'product-statistics/<int:product_id>/',
        ProductStatisticsViewSet.as_view({'get': 'list'})
    ),

]