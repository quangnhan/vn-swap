from django.contrib import admin
from .models import MainTransaction

# Register your models here.

class MainTransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'bank_brand_name', 'account_number', 'amount_in', 'amount_out', 'status', 'created_date')
    ordering = ('-created_date',) 

admin.site.register(MainTransaction, MainTransactionAdmin)