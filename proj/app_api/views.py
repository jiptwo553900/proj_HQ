from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from proj.app_product.models import (
    Product,
    Lesson,
    LessonHistory,
)
from proj.app_api.serializers import (
    UserSerializer,
    ProductSerializer,
    LessonSerializer,
    LessonHistorySerializer,
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for users.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True)
    def user_lessons(self, request, pk=None):
        return Response(data={'test': 'test'})


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for products.
    """
    queryset = Product.objects.none()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.IsAdminUser]
        else:
            self.permission_classes = [permissions.IsAuthenticated]

        return super(ProductViewSet, self).get_permissions()

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            return Product.objects.all()

        return Product.objects.filter(customers=current_user).order_by('id')


class LessonViewSet(viewsets.ModelViewSet):
    """
    API endpoint for lessons.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.IsAdminUser]
        else:
            self.permission_classes = [permissions.IsAuthenticated]

        return super(LessonViewSet, self).get_permissions()


class LessonHistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for lessons history.
    """
    queryset = LessonHistory.objects.none()
    serializer_class = LessonHistorySerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.IsAdminUser]
        else:
            self.permission_classes = [permissions.IsAuthenticated]

        return super(LessonHistoryViewSet, self).get_permissions()

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            return LessonHistory.objects.all()

        return LessonHistory.objects.filter(user=current_user).order_by('-last_viewed_at')