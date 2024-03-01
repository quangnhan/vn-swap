import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import SePayTransaction
from datetime import datetime

# Create your views here.

def download_all_sepay_transaction(request):

    API_TOKEN = "FJQDBAFNR6BODENYYVFDKL9I8MWPH8SVCBR1OZQY4OPZAGVSQTPTAXEGRW3KW1QH"
    url = "https://my.sepay.vn/userapi/transactions/list"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }

    try:
        response = requests.get(f"{url}/", headers=headers)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Result: ", response.json())
            transactions = response.json().get("transactions", [])
            for transaction in transactions:
                sepay_transaction = SePayTransaction(
                    transaction_id = transaction["transaction_id"],
                    transaction_date = datetime.strptime(transaction['transaction_date'], "%Y-%m-%d %H:%M:%S"),
                    account_number = transaction["account_number"],
                    sub_account = transaction["sub_account"],
                    amount_in = transaction["amount_in"],
                    amount_out = transaction["amount_out"],
                    accumulated = transaction["accumulated"],
                    transaction_content = transaction["transaction_content"],
                    reference_number = transaction["reference_number"],
                    bank_brand_name = transaction["bank_brand_name"],
                    bank_account_id = transaction["bank_account_id"],
                )
                sepay_transaction.save()
        else:
            # Print error message if the request was not successful
            print("Error:", response.status_code)
            # Optionally, you can raise an exception to handle non-200 status codes differently
            response.raise_for_status()
    except requests.RequestException as e:
        # Catch any exceptions that occurred during the request (e.g., network errors)
        print("An error occurred:", e)

    return HttpResponse("Download successfully")