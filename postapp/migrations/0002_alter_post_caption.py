# Generated by Django 4.1.4 on 2023-07-03 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(max_length=100),
        ),
    ]
