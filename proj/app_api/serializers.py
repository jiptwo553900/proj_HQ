from django.contrib.auth.models import User
from rest_framework import serializers

from proj.app_product.models import (
    Product,
    Lesson,
    LessonHistory,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'email',
            'products',

        ]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # owner = UserSerializer()

    class Meta:
        model = Product
        fields = [
            'name',
            'owner',
            'customers',
            'lessons',

        ]


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonHistorySerializer(serializers.HyperlinkedModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = LessonHistory
        fields = [
            'url',
            'user',
            'lesson',
            'is_viewed',
            'viewing_time_seconds',
            'last_viewed_at',
        ]
