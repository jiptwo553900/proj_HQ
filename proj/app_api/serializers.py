from rest_framework import serializers

from proj.app_product.models import Lesson


class UserLessonsSerializer(serializers.ModelSerializer):
    is_viewed = serializers.BooleanField()
    viewed_time = serializers.IntegerField()

    class Meta:
        model = Lesson
        fields = ('headline', 'is_viewed', 'viewed_time', )


class UserLessonsByProductSerializer(serializers.ModelSerializer):
    is_viewed = serializers.BooleanField()
    viewed_time = serializers.IntegerField()
    last_viewed = serializers.DateTimeField()

    class Meta:
        model = Lesson
        fields = ('headline', 'is_viewed', 'viewed_time', 'last_viewed', )


class ProductStatisticsSerializer(serializers.Serializer):
    title = serializers.CharField()
    total_lessons_viewed = serializers.IntegerField()
    total_view_time = serializers.IntegerField()
    total_users_have_access_count = serializers.IntegerField()
    purchase_percent = serializers.FloatField()