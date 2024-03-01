from django.http import HttpResponse
from .utils.solana_manager import SolanaManager
from sepay.models import SePayTransaction
# Create your views here.

def solana_send_transaction(request):
    solana_manager = SolanaManager()
    wallet_address = "27FjaLmnwvyoNQ6N6SRnpTQMMSxFGuPf1hBLewx7YtJZ"
    amount = 10000000

    result = solana_manager.send_transaction(wallet_address, amount)
    return HttpResponse(result)

def solana_sepay_send_transaction(request):
    solana_manager = SolanaManager()
    transaction_id = 229086

    sepay_transaction = SePayTransaction.objects.get(transaction_id=transaction_id)
    wallet_address = sepay_transaction.transaction_content
    amount = 10000000

    result = solana_manager.send_transaction(wallet_address, amount)
    return HttpResponse(result)