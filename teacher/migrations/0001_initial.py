# Generated by Django 2.2.1 on 2019-05-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('e_mail', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=70)),
                ('date_joined', models.DateField()),
                ('proffessional', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
    ]
