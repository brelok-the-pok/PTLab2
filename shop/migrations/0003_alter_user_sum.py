# Generated by Django 4.0 on 2021-12-14 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sum',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
