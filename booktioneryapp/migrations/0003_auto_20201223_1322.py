# Generated by Django 2.2.4 on 2020-12-23 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktioneryapp', '0002_auto_20201223_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default='user', on_delete=django.db.models.deletion.CASCADE, related_name='role_users', to='booktioneryapp.Role'),
        ),
    ]