import logging
from django.db.models.signals import pre_save
from django.dispatch import receiver
from swap.models import SwapTransaction
from swap.utils.solana_manager import SolanaManager
from .models import WAITING_BANK_TRANSFER, MainTransaction, CREATED, COMPLETE_BANK_TRANSFER, CREATE_CRYPTO_TRANSER, COMPLETE_CRYPTO_TRANSFER, COMPLETED

logger = logging.getLogger(__name__)

@receiver(pre_save, sender=MainTransaction)
def sepay_transaction_created(sender, instance, **kwargs):
    if instance.status == CREATED:
        instance.status = WAITING_BANK_TRANSFER

    if instance.status == COMPLETE_BANK_TRANSFER:
        solana_manager = SolanaManager()
        try:
            SwapTransaction.objects.create(
                transaction=instance,
                destination=instance.receiver_wallet_address,
                lamports=instance.amount_out * 10**9,
                source=solana_manager.sender.public_key,  # Assuming sender is a Keypair
            )
            instance.status = CREATE_CRYPTO_TRANSER
        except Exception as e:
            # Handle the exception appropriately, such as logging the error
            logger.error(f"Error creating SwapTransaction: {e}")    

    
    if instance.status == COMPLETE_CRYPTO_TRANSFER:
        instance.status = COMPLETED