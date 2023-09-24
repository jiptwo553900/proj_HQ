from django.contrib.auth.models import User
from rest_framework import serializers

from proj.app_product.models import (
    Product,
    Lesson,
    LessonHistory,
)


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='users-detail')

    class Meta:
        model = User
        # fielsd = '__all__'
        fields = ['id', 'url', 'username', 'is_superuser', 'products_owned', 'products_bought']


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='products-detail')
    owner = serializers.ReadOnlyField(source='owner.username')
    # lessons = serializers.HyperlinkedIdentityField(many=True, view_name='lessons-detail')

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['id', 'url', 'title', 'owner', 'bought_by', 'lessons']



class LessonSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='lessons-detail')
    video_url = serializers.ReadOnlyField()
    duration_seconds = serializers.ReadOnlyField()
    # products = serializers.HyperlinkedIdentityField(many=True, view_name='products-detail')
    # products = ProductSerialiser()

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonHistorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='lesson-history-detail')
    is_viewed = serializers.ReadOnlyField()

    class Meta:
        model = LessonHistory
        fields = '__all__'


class ProductSerializerShort(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='products-detail')
    owner = serializers.ReadOnlyField(source='owner.username')
    # lessons = serializers.HyperlinkedIdentityField(many=True, view_name='lessons-detail')

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['id', 'url', 'title', 'owner', 'lessons']