# Generated by Django 3.1 on 2020-10-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosBackend', '0050_historial_rosas'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial_rosas',
            name='fecha_publicacion',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
