import uuid
from django.db import models

CREATED = 'CREATED'
WAITING_BANK_TRANSFER = 'WAITING_BANK_TRANSFER'
COMPLETE_BANK_TRANSFER = 'COMPLETE_BANK_TRANSFER'
CREATE_CRYPTO_TRANSER = 'CREATE_CRYPTO_TRANSER'
COMPLETE_CRYPTO_TRANSFER = 'COMPLETE_CRYPTO_TRANSFER'
COMPLETED = 'COMPLETED'
FAILED = 'CREAFAILEDTED'

STATUS_CHOICES = (
    (CREATED, 'Created'),
    (WAITING_BANK_TRANSFER, 'Waiting bank transfer'),
    (COMPLETE_BANK_TRANSFER, 'Completed bank transfer'),
    (CREATE_CRYPTO_TRANSER, 'Created crypto transaction'),
    (COMPLETE_CRYPTO_TRANSFER, 'Completed crypto transaction'),
    (COMPLETED, 'Completed'),
    (FAILED, 'Failed'),
)

BANK_CHOICES = (
    ('OCB', 'OCB'),
)

CURRENCY_CHOICES = (
    ('vnd', 'VND'),
    ('sol', 'SOL'),
)

class MainTransaction(models.Model):
    transaction_id = models.CharField(max_length=100, unique=True, blank=True)   
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=CREATED)
    bank_brand_name = models.CharField(max_length=10, choices=BANK_CHOICES, default='ocb')
    sub_account = models.CharField(max_length=20)
    amount_in = models.FloatField()
    in_currency_unit_id = models.CharField(max_length=20, choices=CURRENCY_CHOICES, default='vnd')
    receiver_wallet_address = models.CharField(max_length=100)
    amount_out = models.FloatField()
    out_currency_unit_id = models.CharField(max_length=20, choices=CURRENCY_CHOICES, default='sol')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = uuid.uuid4().hex
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"[Transaction] Id: {self.transaction_id}"