# Generated by Django 4.1.4 on 2022-12-30 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Images/')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BakeryApp.categorymodel')),
            ],
        ),
    ]
