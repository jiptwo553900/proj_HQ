# Generated by Django 4.2.5 on 2023-09-26 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0002_alter_lessonhistory_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bought_by',
        ),
    ]