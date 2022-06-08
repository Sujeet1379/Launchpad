# Generated by Django 3.2.12 on 2022-05-11 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course_overviews', '0027_courseliveclasses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseliveclasses',
            name='client_token',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='courseliveclasses',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='courseliveclasses',
            name='created_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='courseliveclasses',
            name='meeting_link',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='courseliveclasses',
            name='room_key',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='courseliveclasses',
            name='room_name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='courseliveclasses',
            name='topic_name',
            field=models.CharField(max_length=60, null=True),
        ),
    ]