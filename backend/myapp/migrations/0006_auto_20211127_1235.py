# Generated by Django 3.2.9 on 2021-11-27 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_flight_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='partners')),
            ],
        ),
        migrations.RemoveField(
            model_name='package',
            name='activities',
        ),
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='package',
            name='type',
            field=models.CharField(choices=[('group', 'group'), ('custom', 'custom')], default='group', max_length=100),
        ),
    ]
