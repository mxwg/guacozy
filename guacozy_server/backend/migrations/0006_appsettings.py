# Generated by Django 2.2.6 on 2019-10-09 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defaultGuacdServer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.GuacdServer')),
            ],
            options={
                'verbose_name': 'Application Settings',
                'verbose_name_plural': 'Application Settings',
            },
        ),
    ]