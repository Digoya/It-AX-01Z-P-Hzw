# Generated by Django 2.0.5 on 2018-06-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('journal', '0021_auto_20180602_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('email_key', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]