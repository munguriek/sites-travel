# Generated by Django 3.2.9 on 2021-11-30 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_driver_permit_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='permit',
            field=models.FileField(default=1, upload_to='permits'),
            preserve_default=False,
        ),
    ]
