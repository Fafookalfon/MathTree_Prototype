# Generated by Django 3.2.4 on 2021-07-08 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0007_chapter_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='x_position',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='y_position',
            field=models.FloatField(default=0),
        ),
    ]
