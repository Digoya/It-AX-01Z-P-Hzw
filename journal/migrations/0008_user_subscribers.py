# Generated by Django 2.0.5 on 2018-06-01 07:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('journal', '0007_auto_20180601_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subscribers',
            field=models.ManyToManyField(blank=True, null=True, related_name='_user_subscribers_+', to='journal.User'),
        ),
    ]