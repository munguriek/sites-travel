# Generated by Django 3.2.9 on 2021-11-25 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accomadation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('budget', models.CharField(choices=[('budget', 'budget'), ('mid range', 'mid range'), ('up market', 'up market')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='gallery')),
                ('caption', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='PackageCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.CharField(choices=[('budget', 'budget'), ('mid range', 'mid range'), ('up market', 'up market')], max_length=100)),
                ('car', models.CharField(max_length=100)),
                ('driver', models.CharField(choices=[('driver', 'driver'), ('self', 'self')], max_length=100)),
                ('trip', models.CharField(choices=[('Up Country', 'Up Country'), ('Town Service', 'Town Service')], max_length=100)),
                ('pickup', models.CharField(max_length=100)),
                ('dropoff', models.CharField(max_length=100)),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('departure_date', models.DateField(max_length=100)),
                ('adults', models.PositiveIntegerField()),
                ('children', models.PositiveIntegerField()),
                ('infants', models.PositiveIntegerField()),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.flight')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('group', 'group'), ('custom', 'custom')], max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('slots', models.PositiveIntegerField(default=0)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('price', models.PositiveIntegerField()),
                ('activities', models.CharField(choices=[('group', 'group'), ('custom', 'custom')], max_length=200)),
                ('pickup', models.CharField(max_length=100)),
                ('dropoff', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=20)),
                ('arrival_accomodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_accom', to='myapp.accomadation')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.packagecategory')),
                ('trip_accomodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_accom', to='myapp.accomadation')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.packagecategory')),
            ],
        ),
    ]
