# Generated by Django 4.0 on 2022-11-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent', '0004_remove_savead_landmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savead',
            name='pin_no',
            field=models.IntegerField(null=True),
        ),
    ]
