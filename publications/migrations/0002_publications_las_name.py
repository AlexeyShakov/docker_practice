# Generated by Django 4.1.1 on 2022-09-29 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publications',
            name='las_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]