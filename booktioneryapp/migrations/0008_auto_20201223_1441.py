# Generated by Django 2.2.4 on 2020-12-23 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktioneryapp', '0007_auto_20201223_1426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='cat',
        ),
    ]
