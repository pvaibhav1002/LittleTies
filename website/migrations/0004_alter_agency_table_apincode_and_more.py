# Generated by Django 4.2.1 on 2023-10-31 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_customuser_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency_table',
            name='apincode',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='user_table',
            name='upincode',
            field=models.PositiveBigIntegerField(),
        ),
    ]
