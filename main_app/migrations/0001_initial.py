# Generated by Django 2.2.6 on 2019-12-14 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=140)),
                ('common_name', models.CharField(max_length=140)),
                ('color', models.CharField(max_length=140)),
                ('native_location', models.CharField(max_length=140)),
            ],
        ),
    ]