# Generated by Django 5.0.2 on 2024-03-01 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sepay', '0002_alter_sepaytransaction_accumulated_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sepaytransaction',
            name='bank_account_id',
        ),
    ]