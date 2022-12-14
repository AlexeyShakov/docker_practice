# Generated by Django 4.1.1 on 2022-10-02 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_publications_email_publications_patronim_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField(max_length=10)),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.publications')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.template')),
            ],
        ),
    ]
