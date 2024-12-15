# Generated by Django 5.0.4 on 2024-05-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0003_review_alter_car_price_alter_car_speed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='speed',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
