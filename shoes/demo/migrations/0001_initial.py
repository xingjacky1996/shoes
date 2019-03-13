# Generated by Django 2.1.4 on 2019-03-12 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20)),
                ('size', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.AddField(
            model_name='shoes',
            name='u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.User'),
        ),
    ]