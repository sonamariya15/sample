# Generated by Django 4.2.6 on 2024-02-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_request_deid_remove_request_kitid'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.CharField(default='request', max_length=40, null=True),
        ),
    ]
