import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class SePayManager:
    def __init__(self):
        self.url = os.getenv('SEPAY_URL')
        API_TOKEN = os.getenv('SEPAY_API_TOKEN')
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_TOKEN}"
        }

    def get_transaction_list(self):
        response = requests.get(f"{self.url}/userapi/transactions/list", headers=self.headers)
        transactions = []

        try:
            if response.status_code == 200:
                transactions = response.json().get("transactions", [])
            else:
                # Print error message if the request was not successful
                print("Error:", response.status_code)
                # Optionally, you can raise an exception to handle non-200 status codes differently
        except requests.RequestException as e:
            # Catch any exceptions that occurred during the request (e.g., network errors)
            print("An error occurred:", e)

        return transactions

