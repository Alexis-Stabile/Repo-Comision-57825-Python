# Generated by Django 4.1 on 2023-10-08 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.TextField(max_length=40),
        ),
    ]
