from django.urls import path
from .views import solana_send_transaction, solana_sepay_send_transaction

urlpatterns = [
    path('solana/send_transaction/', solana_send_transaction),
    path('solana/sepay/send_transaction/', solana_sepay_send_transaction),
]
