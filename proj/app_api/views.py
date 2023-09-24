from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from proj.app_product.models import Product, Lesson, LessonHistory
from proj.app_api.serializers import UserSerializer, ProductSerializer, LessonSerializer, LessonHistorySerializer, ProductSerializerShort


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAdminUser]


class LessonHistoryViewSet(viewsets.ModelViewSet):
    queryset = LessonHistory.objects.all()
    serializer_class = LessonHistorySerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        viewed_time = self.request.data.get('viewed_time')
        lesson = Lesson.objects.get(id=self.request.data.get('lesson'))
        serializer.save(is_viewed=float(viewed_time) >= lesson.duration_seconds * 0.8)


class LessonsDetailsForUser(viewsets.ReadOnlyModelViewSet):
    queryset = LessonHistory.objects.none()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LessonHistorySerializer

    def get_queryset(self):
        current_user = self.request.user
        products = Product.objects.filter(bought_by=current_user)
        lessons = Lesson.objects.filter(products__in=products)
        qs = LessonHistory.objects.filter(user=current_user, lesson__in=lessons)
        return qs

class ProductDetailsForUser(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.none()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializerShort

    def get_queryset(self):
        current_user = self.request.user
        products = Product.objects.filter(bought_by=current_user)
        return products