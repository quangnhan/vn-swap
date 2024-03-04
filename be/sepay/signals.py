import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from sepay.models import SePayTransaction
from transaction.models import FAILED, MainTransaction, WAITING_BANK_TRANSFER, COMPLETE_BANK_TRANSFER

logger = logging.getLogger(__name__)


# Update status of MainTransaction from WAITING_BANK_TRANSFER to COMPLETE_BANK_TRANSFER
@receiver(post_save, sender=SePayTransaction)
def transfer_money_successfully(sender, instance, created, **kwargs):
    if created:
        try:
            transaction_id = instance.transaction_content.strip()
            main_transaction = MainTransaction.objects.get(
                transaction_id=instance.transaction_content.strip(), # Bank message is transaction ID
                status=WAITING_BANK_TRANSFER,
            )

            if main_transaction.bank_brand_name != instance.bank_brand_name:
                error = f"SePayTransaction [{instance.transaction_id}]: bank_brand_name {main_transaction.bank_brand_name} doesn't match with {instance.bank_brand_name}"
                main_transaction.status = FAILED
                main_transaction.log = error
                main_transaction.save()
                raise ValueError(error)

            if main_transaction.account_number != instance.account_number:
                error = f"SePayTransaction [{instance.transaction_id}]: account_number {main_transaction.account_number} doesn't match with {instance.account_number}"
                main_transaction.status = FAILED
                main_transaction.log = error
                main_transaction.save()
                raise ValueError(error)
            
            if float(main_transaction.amount_in) != float(instance.amount_in):
                error = f"SePayTransaction [{instance.transaction_id}]: amount_in {main_transaction.amount_in} doesn't match with {instance.amount_in}" 
                main_transaction.status = FAILED
                main_transaction.log = error
                main_transaction.save()
                raise ValueError(error)

            main_transaction.status = COMPLETE_BANK_TRANSFER
            main_transaction.save()
        except MainTransaction.DoesNotExist:
            logger.error(f"MainTransaction with ID '{transaction_id}' and status {WAITING_BANK_TRANSFER} does not exist.")
        except ValueError as e:
            logger.error(f"transfer_money_successfully ValueError: {e}")
        except Exception as e:
            logger.error(f"An error occurred: {e}")