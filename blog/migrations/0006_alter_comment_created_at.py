# Generated by Django 3.2.19 on 2023-07-03 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(blank=True, max_length=40, null=True, verbose_name='Date And Time'),
        ),
    ]
