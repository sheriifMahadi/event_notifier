# Generated by Django 3.2.12 on 2022-03-20 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_notifier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='birthdate',
            field=models.DateTimeField(help_text='Date of Birth'),
        ),
    ]
