# Generated by Django 4.2.5 on 2023-09-22 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0002_remove_lesson_products_product_lessons_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lessonhistory',
            options={'verbose_name': ('Lesson History',), 'verbose_name_plural': 'Lesson History'},
        ),
        migrations.RemoveField(
            model_name='lessonhistory',
            name='viewed',
        ),
    ]