import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from transaction.models import MainTransaction, CREATE_CRYPTO_TRANSER, COMPLETE_CRYPTO_TRANSFER, FAILED
from .utils.solana_manager import SolanaManager
from .models import SwapTransaction

logger = logging.getLogger(__name__)

@receiver(post_save, sender=MainTransaction)
def send_crypto_to_receiver(sender, instance, created, **kwargs):
    if instance.status == CREATE_CRYPTO_TRANSER:
        try:
            # Get transaction information
            swap_transaction = SwapTransaction.objects.get(transaction=instance)
            solana_manager = SolanaManager()
            receiver_wallet_address = swap_transaction.destination
            amount = swap_transaction.lamports

            # Send solana
            signature = solana_manager.send_transaction(receiver_wallet_address, amount)

            # Save transction signature
            swap_transaction.signature = str(signature)
            swap_transaction.save()

            # Update status of MainTransction to COMPLETE_CRYPTO_TRANSFER
            instance.status = COMPLETE_CRYPTO_TRANSFER
        except Exception as e:
            error = f"An error occurred while processing MainTransaction object {instance.transaction_id}: {e}"
            instance.status = FAILED
            instance.log = error

            # Log the exception
            logger.error(error)

        # Save MainTransaction status
        instance.save()