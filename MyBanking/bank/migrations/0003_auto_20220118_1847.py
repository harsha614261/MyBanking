# Generated by Django 3.2.11 on 2022-01-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20220118_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='Email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='query',
            name='Name',
            field=models.CharField(max_length=100),
        ),
    ]
