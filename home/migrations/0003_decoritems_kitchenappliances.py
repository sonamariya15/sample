# Generated by Django 4.2.6 on 2024-02-05 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_registration_user_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='DecorItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('desc', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField(null=True)),
                ('profile', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='KitchenAppliances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('desc', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField(null=True)),
                ('profile', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]