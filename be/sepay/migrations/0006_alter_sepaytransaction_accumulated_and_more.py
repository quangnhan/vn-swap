# Generated by Django 5.0.2 on 2024-03-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sepay', '0005_alter_sepaytransaction_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sepaytransaction',
            name='accumulated',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sepaytransaction',
            name='amount_in',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sepaytransaction',
            name='amount_out',
            field=models.FloatField(),
        ),
    ]
