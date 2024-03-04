from django.db import models
from transaction.models import MainTransaction

class SwapTransaction(models.Model):
    transaction = models.OneToOneField(MainTransaction, on_delete=models.CASCADE)
    signature = models.CharField(max_length=100, default='')
    destination = models.CharField(max_length=100)
    lamports = models.IntegerField()
    source = models.CharField(max_length=100)
    confirmation_status = models.CharField(max_length=30, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
