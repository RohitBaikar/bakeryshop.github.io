# Generated by Django 4.1.4 on 2022-12-31 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BakeryApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_title', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='Images/')),
                ('price', models.IntegerField()),
                ('Qua', models.IntegerField()),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BakeryApp.categorymodel')),
            ],
        ),
        migrations.DeleteModel(
            name='ImageModel',
        ),
    ]
