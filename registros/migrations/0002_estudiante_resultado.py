# Generated by Django 3.1.1 on 2020-09-03 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='resultado',
            field=models.CharField(default='', max_length=48),
            preserve_default=False,
        ),
    ]
