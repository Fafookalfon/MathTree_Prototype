# Generated by Django 3.2.4 on 2021-07-08 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0005_remove_chapter_prerequisites'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='chapterpage',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coursetree',
            name='data',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='hints',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='questions',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='solutions',
            field=models.TextField(default=''),
        ),
    ]