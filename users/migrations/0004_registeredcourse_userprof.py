# Generated by Django 4.0.1 on 2022-01-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_registeredcourse_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredcourse',
            name='userprof',
            field=models.ManyToManyField(to='users.Profile'),
        ),
    ]
