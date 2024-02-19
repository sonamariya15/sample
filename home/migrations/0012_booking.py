# Generated by Django 4.2.6 on 2024-02-08 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_feedback_deid_remove_feedback_kitid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=100, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('status', models.CharField(default='Processing', max_length=40, null=True)),
                ('deid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.decoritems')),
                ('kitid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.kitchenappliances')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.registration_user')),
            ],
        ),
    ]