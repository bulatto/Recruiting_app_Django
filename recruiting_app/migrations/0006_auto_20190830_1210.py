# Generated by Django 2.2.4 on 2019-08-30 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting_app', '0005_auto_20190830_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='isHandOfShadow',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='isTested',
            field=models.BooleanField(default=False),
        ),
    ]
