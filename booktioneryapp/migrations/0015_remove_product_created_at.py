# Generated by Django 2.2.4 on 2020-12-26 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktioneryapp', '0014_auto_20201226_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
    ]