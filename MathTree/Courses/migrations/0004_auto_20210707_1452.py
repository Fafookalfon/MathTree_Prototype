# Generated by Django 3.2.4 on 2021-07-07 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0003_chapter_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='x_position',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='y_position',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Prerequisite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('prerequisite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prerequisite', to='Courses.course')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to='Courses.course')),
            ],
        ),
    ]
