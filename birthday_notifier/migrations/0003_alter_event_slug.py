# Generated by Django 3.2.12 on 2022-03-31 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_notifier', '0002_alter_event_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
