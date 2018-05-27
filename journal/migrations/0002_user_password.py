# Generated by Django 2.0.5 on 2018-05-27 09:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, help_text='Enter your password', max_length=40),
            preserve_default=False,
        ),
    ]