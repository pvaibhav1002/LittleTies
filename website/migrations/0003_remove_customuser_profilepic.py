# Generated by Django 4.2.1 on 2023-05-30 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_customuser_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profilepic',
        ),
    ]
