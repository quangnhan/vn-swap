# Generated by Django 5.0.2 on 2024-03-03 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_alter_transaction_bank_brand_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('waiting_bank_transfer', 'Waiting bank transfer'), ('complete_bank_transfer', 'Completed bank transfer'), ('create_crypto_transaction', 'Created crypto transaction'), ('complete_crypto_transaction', 'Completed crypto transaction'), ('completed', 'Completed'), ('failed', 'Failed')], default='created', max_length=30),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
