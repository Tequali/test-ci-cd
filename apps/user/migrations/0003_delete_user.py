# Generated by Django 5.1.6 on 2025-02-26 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_user_info2_alter_user_user_info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
