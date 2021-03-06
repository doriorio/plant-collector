# Generated by Django 2.2.6 on 2019-12-17 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_plant_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_type', models.CharField(choices=[('C', 'Culinary'), ('H', 'Homeopathic'), ('T', 'Topical'), ('A', 'Aromatic'), ('M', 'Medicinal')], max_length=1)),
                ('description', models.CharField(default='', max_length=480)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Plant')),
            ],
        ),
    ]
