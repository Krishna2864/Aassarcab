# Generated by Django 4.0 on 2021-12-20 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cab_Service', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fuel_Mangement',
            new_name='Fuel_Management',
        ),
        migrations.RenameModel(
            old_name='Refral_Mangemnt',
            new_name='Refral_Managemnt',
        ),
        migrations.RenameModel(
            old_name='Seat_Mangement',
            new_name='Seat_Management',
        ),
    ]
