# Generated by Django 4.2.6 on 2024-02-13 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(default='Booking Confirmed', max_length=40, null=True),
        ),
    ]
