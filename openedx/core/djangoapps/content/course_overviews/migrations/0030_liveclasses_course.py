# Generated by Django 3.2.12 on 2022-06-02 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_overviews', '0029_auto_20220516_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='liveclasses',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course_overviews.courseoverview'),
        ),
    ]