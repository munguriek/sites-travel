# Generated by Django 3.2.9 on 2021-11-30 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_driver_permit_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='permit_class',
            field=models.CharField(default='DL', max_length=100),
        ),
    ]
