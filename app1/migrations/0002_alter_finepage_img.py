# Generated by Django 4.2.3 on 2023-07-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finepage',
            name='img',
            field=models.URLField(max_length=1000),
        ),
    ]