from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='products_owned')

    class Meta:
        verbose_name = 'Product',
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'ProductAccess',
        verbose_name_plural = 'ProductAccesses'

    def __str__(self):
        return f'{self.user.username} - {self.product.id}. {self.product.title}'


class Lesson(models.Model):
    headline = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, related_name='lessons')
    video_url = models.URLField(default='https://ya.ru/')
    duration_seconds = models.PositiveIntegerField(default=200)

    class Meta:
        verbose_name = 'Lesson',
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.headline


class LessonHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='history')
    viewed_time = models.PositiveIntegerField(default=0)
    is_viewed = models.BooleanField(default=False)
    last_viewed = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'lesson')
        verbose_name = 'Lesson History',
        verbose_name_plural = 'Lesson History'

    def __str__(self):
        return f'{self.user.username} - {self.lesson.id}. {self.lesson.headline}'
