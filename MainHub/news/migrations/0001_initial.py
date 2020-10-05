# Generated by Django 3.1.2 on 2020-10-04 15:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='Slider')),
                ('status', models.BooleanField(default=0)),
                ('created_at', models.DateField()),
                ('slug', models.CharField(max_length=150, unique=True)),
            ],
        ),
    ]
