import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from sepay.models import SePayTransaction
from transaction.models import MainTransaction, WAITING_BANK_TRANSFER, COMPLETE_BANK_TRANSFER

logger = logging.getLogger(__name__)


# Update status of MainTransaction from WAITING_BANK_TRANSFER to COMPLETE_BANK_TRANSFER
@receiver(post_save, sender=SePayTransaction)
def sepay_transaction_created(sender, instance, created, **kwargs):
    if created:
        try:
            transaction_id = instance.transaction_content.strip()
            main_transaction = MainTransaction.objects.get(
                transaction_id=instance.transaction_content.strip(), # Bank message is transaction ID
                bank_brand_name=instance.bank_brand_name,
                sub_account=instance.sub_account,
                amount_in=instance.amount_in,
                status=WAITING_BANK_TRANSFER,
            )
            main_transaction.status = COMPLETE_BANK_TRANSFER
            main_transaction.save()
        except MainTransaction.DoesNotExist:
            logger.error(f"MainTransaction with ID {transaction_id} and status {WAITING_BANK_TRANSFER} does not exist.")
        except Exception as e:
            logger.error(f"An error occurred: {e}")