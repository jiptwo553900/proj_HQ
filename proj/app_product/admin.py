from django.contrib import admin

from proj.app_product.models import Product, Lesson, LessonHistory

# Register your models here.
admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(LessonHistory)