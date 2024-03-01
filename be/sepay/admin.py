from django.contrib import admin
from .models import SePayTransaction

# Register your models here.

class SePayTransactionAdmin(admin.ModelAdmin):
    pass

admin.site.register(SePayTransaction, SePayTransactionAdmin)
