# Generated by Django 3.1.3 on 2021-01-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
