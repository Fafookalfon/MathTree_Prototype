# Generated by Django 3.2.4 on 2021-07-15 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0009_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
