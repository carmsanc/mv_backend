# Generated by Django 3.1 on 2020-08-24 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosBackend', '__first__'),
        ('serviciosBackend', '0020_auto_20200824_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
