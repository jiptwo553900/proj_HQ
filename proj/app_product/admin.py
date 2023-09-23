from django.contrib import admin

from .models import Product, Lesson, LessonHistory

# Register your models here.

@admin.register(Product, Lesson, LessonHistory)
class PersonAdmin(admin.ModelAdmin):
    pass