# Generated by Django 3.1 on 2020-11-06 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20201106_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
