# Generated by Django 3.2.11 on 2022-01-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='Contact',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='query',
            name='Querymes',
            field=models.TextField(max_length=100),
        ),
    ]
