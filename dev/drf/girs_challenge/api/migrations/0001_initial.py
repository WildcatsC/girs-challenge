# Generated by Django 4.0.5 on 2022-06-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', models.JSONField(default=dict)),
                ('wear', models.DateField(default=0)),
                ('weather', models.DateField(default=0)),
                ('vegetation', models.DateField(default=0)),
                ('names', models.CharField(default='', max_length=50, unique=True)),
            ],
        ),
    ]