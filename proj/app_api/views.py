from django.contrib.auth.models import User
from django.db.models import FilteredRelation, Q, F, Count, OuterRef, Sum
from rest_framework import viewsets, mixins, permissions, exceptions

from proj.app_api.serializers import UserLessonsSerializer, UserLessonsByProductSerializer, ProductStatisticsSerializer
from proj.app_product.models import ProductAccess, Lesson, Product, LessonHistory


class UserLessonsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = UserLessonsSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        current_user = self.request.user
        accesses = ProductAccess.objects.filter(user=current_user)

        qs = Lesson.objects.filter(
            products__in=accesses.values('product_id')
        ).alias(
            details=FilteredRelation(
                relation_name='history',
                condition=Q(history__user=current_user)
            )
        ).annotate(
            is_viewed=F('details__is_viewed'),
            viewed_time=F('details__viewed_time')
        )

        return qs


class UserLessonsByProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = UserLessonsByProductSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        current_user = self.request.user
        accesses = ProductAccess.objects.filter(user=current_user)
        product_id = self.kwargs['product_id']

        if not (product_id in accesses.values_list('product_id', flat=True)):
            raise exceptions.NotFound

        qs = Lesson.objects.filter(
            products=product_id
        ).alias(
            details=FilteredRelation(
                relation_name='history',
                condition=Q(history__user=current_user)
            )
        ).annotate(
            is_viewed=F('details__is_viewed'),
            viewed_time=F('details__viewed_time'),
            last_viewed=F('details__last_viewed')
        )

        return qs


class ProductStatisticsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = ProductStatisticsSerializer
    permission_classes = (permissions.IsAdminUser, )

    def get_queryset(self):
        qs = Product.objects.all().annotate(
            total_lessons_viewed=Count(
                LessonHistory.objects.filter(
                    lesson__products=OuterRef('id'),
                    is_viewed=True
                ).values('id')
            ),
            total_view_time=Sum(
                LessonHistory.objects.filter(
                    lesson__products=OuterRef('id')
                ).values('viewed_time')
            ),
            total_users_have_access_count=Count(
                ProductAccess.objects.filter(
                    product_id=OuterRef('id')
                ).values('id')
            ),
            purchase_percent=F('total_users_have_access_count') / float(User.objects.all().count()) * 100
        )

        return qs