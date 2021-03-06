# Generated by Django 2.2.1 on 2019-05-28 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0004_auto_20190528_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('duration_of_course', models.IntegerField(max_length=30)),
                ('start_date', models.DateField(max_length=50)),
                ('end_date', models.DateField(max_length=30)),
                ('Description', models.TextField()),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacher')),
            ],
        ),
    ]
