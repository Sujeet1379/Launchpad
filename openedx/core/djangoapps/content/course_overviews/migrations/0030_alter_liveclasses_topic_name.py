# Generated by Django 3.2.12 on 2022-07-14 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_overviews', '0029_auto_20220714_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liveclasses',
            name='topic_name',
            field=models.CharField(max_length=60, null=True, unique=True),
        ),
    ]