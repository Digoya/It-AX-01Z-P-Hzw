# Generated by Django 2.0.5 on 2018-06-03 10:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('journal', '0022_emailverification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='email_key',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]