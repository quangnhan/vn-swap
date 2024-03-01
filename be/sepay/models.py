from django.db import models

# Create your models here.

class SePayTransaction(models.Model):
    transaction_id = models.CharField(max_length=20)
    transaction_date = models.DateTimeField()
    account_number = models.CharField(max_length=20)
    sub_account = models.CharField(max_length=20)
    amount_in = models.DecimalField(max_digits=15, decimal_places=2)
    amount_out = models.DecimalField(max_digits=15, decimal_places=2)
    accumulated = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_content = models.CharField(max_length=100)
    reference_number = models.CharField(max_length=50)
    bank_brand_name = models.CharField(max_length=50)
    bank_account_id = models.CharField(max_length=50)