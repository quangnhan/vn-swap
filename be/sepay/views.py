import json
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils.sepay_manager import SePayManager
from .models import SePayTransaction

# Create your views here.

@csrf_exempt  # Disable CSRF protection for this view
def webhook_handler(request):
    if request.method == 'POST':
        # Parse the JSON data from the request body
        try:
            webhook_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON payload'}, status=400)

        # Create a new SePayTransaction instance with the parsed data
        transaction_id = webhook_data.get('id')
        sepay_transaction, created = SePayTransaction.objects.get_or_create(
            transaction_id=transaction_id,
            defaults={
                'transaction_date': datetime.strptime(webhook_data.get('transactionDate'), "%Y-%m-%d %H:%M:%S"),
                'account_number': webhook_data.get('accountNumber'),
                'sub_account': webhook_data.get('subAccount'),
                'amount_in': webhook_data.get('transferAmount') if webhook_data.get('transferType') == 'in' else 0,
                'amount_out': webhook_data.get('transferAmount') if webhook_data.get('transferType') == 'out' else 0,
                'accumulated': webhook_data.get('accumulated'),
                'transaction_content': webhook_data.get('content'),
                'reference_number': webhook_data.get('referenceCode'),
                'bank_brand_name': webhook_data.get('gateway'),
            }
        )

        # Save the SePayTransaction instance to the database if it was created
        if created:
            sepay_transaction.save()
            return JsonResponse({'message': f'Create transaction {transaction_id} successfully'})
        else:
            return JsonResponse({'message': f'Transaction {transaction_id} already exist'})
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

def download_all_transaction(request):
    sepay_manager = SePayManager()
    transactions = sepay_manager.get_transaction_list()

    for transaction in transactions:
        # Check if a record with the same transaction_id exists in the database
        sepay_transaction, created = SePayTransaction.objects.get_or_create(
            transaction_id=transaction["id"],
            defaults={
                'transaction_date': datetime.strptime(transaction['transaction_date'], "%Y-%m-%d %H:%M:%S"),
                'account_number': transaction["account_number"],
                'sub_account': transaction["sub_account"],
                'amount_in': transaction["amount_in"],
                'amount_out': transaction["amount_out"],
                'accumulated': transaction["accumulated"],
                'transaction_content': transaction["transaction_content"],
                'reference_number': transaction["reference_number"],
                'bank_brand_name': transaction["bank_brand_name"],
            }
        )
        # If the record was created, save it to the database
        if created:
            sepay_transaction.save()


    return HttpResponse("Download successfully")