import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from sepay.models import SePayTransaction
from .utils.solana_manager import SolanaManager

logger = logging.getLogger(__name__)

@receiver(post_save, sender=SePayTransaction)
def sepay_transaction_created(sender, instance, created, **kwargs):
    if created:
        try:
            # Add your code to be executed when a new SePayTransaction object is created
            print("SePayTransaction object created:", instance.transaction_id)
            # Add any other actions you want to perform here
            solana_manager = SolanaManager()
            wallet_address = instance.transaction_content.strip()
            amount = 10000000

            result = solana_manager.send_transaction(wallet_address, amount)
            print(f"Create transaction {result}")
        except Exception as e:
            # Log the exception
            print(f"An error occurred while processing SePayTransaction object {instance.transaction_id}: {e}")
            # Print a message to the console
            print(f"Error processing SePayTransaction object {instance.transaction_id}: {e}")
