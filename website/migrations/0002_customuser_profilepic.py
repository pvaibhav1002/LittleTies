# Generated by Django 4.2.1 on 2023-05-30 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profilepic',
            field=models.CharField(max_length=200, null=True),
        ),
    ]