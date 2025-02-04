# Generated by Django 4.1 on 2024-07-24 07:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_comment_created_date_alter_post_created_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 24, 7, 48, 45, 850256, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comment",
                to="blog.post",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 24, 7, 48, 45, 849257, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
