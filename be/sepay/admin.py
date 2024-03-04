from django.contrib import admin
from .models import SePayTransaction

# Register your models here.

class SePayTransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'bank_brand_name', 'account_number', 'amount_in', 'transaction_content', 'transaction_date')
    ordering = ('-transaction_id',) 

admin.site.register(SePayTransaction, SePayTransactionAdmin)
