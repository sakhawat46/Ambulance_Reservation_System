# Generated by Django 3.2.9 on 2022-01-19 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn_app', '0003_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
    ]
