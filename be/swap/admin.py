from django.contrib import admin
from .models import SwapTransaction

# Register your models here.

class SwapTransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'signature', 'lamports', 'confirmation_status', 'created_date', 'updated_date')
    ordering = ('-created_date',) 

admin.site.register(SwapTransaction, SwapTransactionAdmin)