# Generated by Django 2.2.1 on 2019-05-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration_of_course',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(),
        ),
    ]
