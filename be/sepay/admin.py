from django.contrib import admin
from .models import SePayTransaction

# Register your models here.

class SePayTransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'account_number', 'sub_account', 'amount_in', 'accumulated', 'transaction_date', 'transaction_content')
    ordering = ('-transaction_id',) 

admin.site.register(SePayTransaction, SePayTransactionAdmin)
