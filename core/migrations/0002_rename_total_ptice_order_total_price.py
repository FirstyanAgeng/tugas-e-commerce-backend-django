# Generated by Django 4.2.5 on 2023-09-20 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_ptice',
            new_name='total_price',
        ),
    ]
