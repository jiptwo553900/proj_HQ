from django.db import models
from django.contrib.auth.models import User


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField(blank=True)
    duration_seconds = models.IntegerField(blank=True)

    class Meta:
        verbose_name = 'Lesson',
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True
    )
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='products'
    )
    customers = models.ManyToManyField(
        to=User,
        blank=True
    )
    lessons = models.ManyToManyField(
        to=Lesson,
        blank=True
    )

    class Meta:
        verbose_name = 'Product',
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class LessonHistory(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE)
    viewing_time_seconds = models.IntegerField(default=0)
    last_viewed_at = models.DateTimeField(auto_now=True)

    @property
    def is_viewed(self):
        lesson = Lesson.objects.get(id=self.id)
        if self.viewing_time_seconds >= lesson.duration_seconds * 0.8:
            return True
        return False

    class Meta:
        verbose_name = 'Lesson History',
        verbose_name_plural = 'Lesson History'

    def __str__(self):
        return f'{self.lesson} - {self.user}'
