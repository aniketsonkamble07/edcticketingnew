# Generated by Django 2.2.28 on 2023-08-12 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketingapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_type',
        ),
    ]
