# Generated by Django 4.2.5 on 2023-09-26 07:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_product', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lessonhistory',
            unique_together={('user', 'lesson')},
        ),
    ]
