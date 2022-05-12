# Generated by Django 3.2.12 on 2022-03-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celebrant', models.CharField(help_text='Celebrant Name', max_length=256)),
                ('birthdate', models.DateField(help_text='Date of Birth')),
                ('slug', models.SlugField(max_length=250)),
            ],
        ),
    ]
