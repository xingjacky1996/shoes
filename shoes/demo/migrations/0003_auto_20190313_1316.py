# Generated by Django 2.1.3 on 2019-03-13 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20190312_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='size',
            field=models.CharField(max_length=11),
        ),
    ]