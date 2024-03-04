from django.db import models

# Create your models here.

class SePayTransaction(models.Model):
    transaction_id = models.CharField(max_length=20, unique=True)
    transaction_date = models.DateTimeField()
    bank_brand_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=20)
    sub_account = models.CharField(max_length=20, null=True, blank=True)
    amount_in = models.FloatField()
    amount_out = models.FloatField()
    accumulated = models.FloatField()
    transaction_content = models.CharField(max_length=100)
    reference_number = models.CharField(max_length=50)

    def __str__(self):
        return f"[SePayTransaction] Transaction ID: {self.transaction_id}"