# Generated by Django 2.0.5 on 2018-06-02 12:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('journal', '0017_auto_20180602_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='/static/journal/images/default.png', upload_to='images/'),
        ),
    ]